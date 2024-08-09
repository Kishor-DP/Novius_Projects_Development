from __future__ import division  # support for python2

from datetime import datetime
import time

#from webgears import json
import json

import Server
import queue
import multiprocessing

from threading import Thread, Condition
import concurrent.futures
import logging
import sys
try:
    from urllib.parse import urlparse
except ImportError:  # support for python2
    from urlparse import urlparse

from opcua import ua
from opcua.client.ua_client import UaClient
from opcua.common.xmlimporter import XmlImporter
from opcua.common.xmlexporter import XmlExporter
from opcua.common.node import Node
from opcua.common.manage_nodes import delete_nodes
from opcua.common.subscription import Subscription
from opcua.common import utils
from opcua.common import ua_utils
from opcua.crypto import security_policies
from opcua.common.shortcuts import Shortcuts
from opcua.common.structures import load_type_definitions, load_enums

use_crypto = True
from gevent import monkey
monkey.patch_all()

try:
    from opcua.crypto import uacrypto
except ImportError:
    use_crypto = False


_logger = logging.getLogger(__name__)
tChat = None
tmpr = None
tempQue = None
# client = None

class KeepAlive(Thread):

    """
    Used by Client to keep the session open.
    OPCUA defines timeout both for sessions and secure channel
    """

    def __init__(self, client, timeout):
        """
        :param session_timeout: Timeout to re-new the session
            in milliseconds.
        """
        Thread.__init__(self)
        _logger = logging.getLogger(__name__)

        self.client = client
        self._dostop = False
        self._cond = Condition()
        self.timeout = timeout

        # some server support no timeout, but we do not trust them
        if self.timeout == 0:
            self.timeout = 3600000  # 1 hour


    def run(self):
        _logger.debug("starting keepalive thread with period of %s milliseconds", self.timeout)
        server_state = self.client.get_node(ua.FourByteNodeId(ua.ObjectIds.Server_ServerStatus_State))
        while not self._dostop:
            with self._cond:
                self._cond.wait(self.timeout / 1000)
            if self._dostop:
                break
            _logger.debug("renewing channel")
            try:
                self.client.open_secure_channel(renew=True)
            except concurrent.futures.TimeoutError:
                _logger.debug("keepalive failed: timeout on open_secure_channel()")
                break
            val = server_state.get_value()
            _logger.debug("server state is: %s ", val)
        _logger.debug("keepalive thread has stopped")



    def stop(self):
        _logger.debug("stoping keepalive thread")
        self._dostop = True
        with self._cond:
            self._cond.notify_all()




class Client(object):
    """
    High level client to connect to an OPC-UA server.

    This class makes it easy to connect and browse address space.
    It attempts to expose as much functionality as possible
    but if you want more flexibility it is possible and advised to
    use the UaClient object, available as self.uaclient, which offers
    the raw OPC-UA services interface.
    """

    if use_crypto is False:
        logging.getLogger(__name__).warning("cryptography is not installed, use of crypto disabled")

    def __init__(self, url, timeout=4):
        """

        :param url: url of the server.
            if you are unsure of url, write at least hostname
            and port and call get_endpoints

        :param timeout:
            Each request sent to the server expects an answer within this
            time. The timeout is specified in seconds.

        Some other client parameters can be changed by setting
        attributes on the constructed object:

        secure_channel_timeout
            Timeout for the secure channel, specified in milliseconds.

        session_timeout
            Timeout for the session, specified in milliseconds.

        See the source code for the exhaustive list.
        """
        _logger = logging.getLogger(__name__)
        self.server_url = urlparse(url)
        # take initial username and password from the url
        self._username = self.server_url.username
        self._password = self.server_url.password
        self.name = "Pure Python Client"
        self.description = self.name
        self.application_uri = "urn:freeopcua:client"
        self.product_uri = "urn:freeopcua.github.io:client"
        self.security_policy = ua.SecurityPolicy()
        self.secure_channel_id = None
        self.secure_channel_timeout = 3600000  # 1 hour
        self.session_timeout = 3600000  # 1 hour
        self._policy_ids = []
        self.uaclient = UaClient(timeout)
        self.user_certificate = None
        self.user_private_key = None
        self._server_nonce = None
        self._session_counter = 1
        self.keepalive = None
        self.nodes = Shortcuts(self.uaclient)
        self.max_messagesize = 0  # No limits
        self.max_chunkcount = 0  # No limits

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()


    @staticmethod
    def find_endpoint(endpoints, security_mode, policy_uri):
        """
        Find endpoint with required security mode and policy URI
        """
        for ep in endpoints:
            if (ep.EndpointUrl.startswith(ua.OPC_TCP_SCHEME) and
                    ep.SecurityMode == security_mode and
                    ep.SecurityPolicyUri == policy_uri):
                return ep
        raise ua.UaError("No matching endpoints: {0}, {1}".format(security_mode, policy_uri))



    def set_user(self, username):
        """
        Set user name for the connection.
        initial user from the URL will be overwritten
        """
        self._username = username



    def set_password(self, pwd):
        """
        Set user password for the connection.
        initial password from the URL will be overwritten
        """
        self._password = pwd



    def set_security_string(self, string):
        """
        Set SecureConnection mode. String format:
        Policy,Mode,certificate,private_key[,server_private_key]
        where Policy is Basic128Rsa15, Basic256 or Basic256Sha256,
            Mode is Sign or SignAndEncrypt
            certificate, private_key and server_private_key are
                paths to .pem or .der files
        Call this before connect()
        """
        if not string:
            return
        parts = string.split(',')
        if len(parts) < 4:
            raise ua.UaError('Wrong format: `{0}`, expected at least 4 comma-separated values'.format(string))
        policy_class = getattr(security_policies, 'SecurityPolicy' + parts[0])
        mode = getattr(ua.MessageSecurityMode, parts[1])
        return self.set_security(policy_class, parts[2], parts[3],
                                 parts[4] if len(parts) >= 5 else None, mode)



    def set_security(self, policy, certificate_path, private_key_path,
                     server_certificate_path=None,
                     mode=ua.MessageSecurityMode.SignAndEncrypt):
        """
        Set SecureConnection mode.
        Call this before connect()
        """
        if server_certificate_path is None:
            # load certificate from server's list of endpoints
            endpoints = self.connect_and_get_server_endpoints()
            endpoint = Client.find_endpoint(endpoints, mode, policy.URI)
            server_cert = uacrypto.x509_from_der(endpoint.ServerCertificate)
        else:
            server_cert = uacrypto.load_certificate(server_certificate_path)
        cert = uacrypto.load_certificate(certificate_path)
        pk = uacrypto.load_private_key(private_key_path)
        self.security_policy = policy(server_cert, cert, pk, mode)
        self.uaclient.set_security(self.security_policy)



    def load_client_certificate(self, path):
        """
        load our certificate from file, either pem or der
        """
        self.user_certificate = uacrypto.load_certificate(path)



    def load_private_key(self, path):
        """
        Load user private key. This is used for authenticating using certificate
        """
        self.user_private_key = uacrypto.load_private_key(path)



    def connect_and_get_server_endpoints(self):
        """
        Connect, ask server for endpoints, and disconnect
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()
            endpoints = self.get_endpoints()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()
        return endpoints



    def connect_and_find_servers(self):
        """
        Connect, ask server for a list of known servers, and disconnect
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()  # spec says it should not be necessary to open channel
            servers = self.find_servers()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()
        return servers



    def connect_and_find_servers_on_network(self):
        """
        Connect, ask server for a list of known servers on network, and disconnect
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()
            servers = self.find_servers_on_network()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()
        return servers



    def connect(self):
        """
        High level method
        Connect, create and activate session
        """
        print("Trying to connect server")
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()
            try:
                self.create_session()
                try:
                    self.activate_session(username=self._username, password=self._password, certificate=self.user_certificate)
                except Exception:
                    # clean up the session
                    self.close_session()
                    raise
            except Exception:
                # clean up the secure channel
                self.close_secure_channel()
                raise
        except Exception:
            self.disconnect_socket()  # clean up open socket
            raise



    def disconnect(self):
        """
        High level method
        Close session, secure channel and socket
        """
        try:
            self.close_session()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()



    def connect_socket(self):
        """
        connect to socket defined in url
        """
        self.uaclient.connect_socket(self.server_url.hostname, self.server_url.port)



    def disconnect_socket(self):
        self.uaclient.disconnect_socket()



    def send_hello(self):
        """
        Send OPC-UA hello to server
        """
        ack = self.uaclient.send_hello(self.server_url.geturl(), self.max_messagesize, self.max_chunkcount)

        # TODO: Handle ua.UaError
        if isinstance(ack, ua.UaStatusCodeError):
            raise ack



    def open_secure_channel(self, renew=False):
        """
        Open secure channel, if renew is True, renew channel
        """
        params = ua.OpenSecureChannelParameters()
        params.ClientProtocolVersion = 0
        params.RequestType = ua.SecurityTokenRequestType.Issue
        if renew:
            params.RequestType = ua.SecurityTokenRequestType.Renew
        params.SecurityMode = self.security_policy.Mode
        params.RequestedLifetime = self.secure_channel_timeout
        # length should be equal to the length of key of symmetric encryption
        params.ClientNonce = utils.create_nonce(self.security_policy.symmetric_key_size) # this nonce is used to create a symmetric key
        result = self.uaclient.open_secure_channel(params)
        if self.secure_channel_timeout != result.SecurityToken.RevisedLifetime:
            _logger.warning("Requested secure channel timeout to be %dms, got %dms instead",
                                self.secure_channel_timeout,
                                result.SecurityToken.RevisedLifetime)
            self.secure_channel_timeout = result.SecurityToken.RevisedLifetime



    def close_secure_channel(self):
        return self.uaclient.close_secure_channel()



    def get_endpoints(self):
        params = ua.GetEndpointsParameters()
        params.EndpointUrl = self.server_url.geturl()
        return self.uaclient.get_endpoints(params)



    def find_servers(self, uris=None):
        """
        send a FindServer request to the server. The answer should be a list of
        servers the server knows about
        A list of uris can be provided, only server having matching uris will be returned
        """
        if uris is None:
            uris = []
        params = ua.FindServersParameters()
        params.EndpointUrl = self.server_url.geturl()
        params.ServerUris = uris
        return self.uaclient.find_servers(params)



    def find_servers_on_network(self):
        params = ua.FindServersOnNetworkParameters()
        return self.uaclient.find_servers_on_network(params)



    def create_session(self):
        """
        send a CreateSessionRequest to server with reasonable parameters.
        If you want o modify settings look at code of this methods
        and make your own
        """
        desc = ua.ApplicationDescription()
        desc.ApplicationUri = self.application_uri
        desc.ProductUri = self.product_uri
        desc.ApplicationName = ua.LocalizedText(self.name)
        desc.ApplicationType = ua.ApplicationType.Client

        params = ua.CreateSessionParameters()
        # at least 32 random bytes for server to prove possession of private key (specs part 4, 5.6.2.2)
        nonce = utils.create_nonce(32)
        params.ClientNonce = nonce
        params.ClientCertificate = self.security_policy.client_certificate
        params.ClientDescription = desc
        params.EndpointUrl = self.server_url.geturl()
        params.SessionName = self.description + " Session" + str(self._session_counter)
        params.RequestedSessionTimeout = self.session_timeout
        params.MaxResponseMessageSize = 0  # means no max size
        response = self.uaclient.create_session(params)
        if self.security_policy.client_certificate is None:
            data = nonce
        else:
            data = self.security_policy.client_certificate + nonce
        self.security_policy.asymmetric_cryptography.verify(data, response.ServerSignature.Signature)
        self._server_nonce = response.ServerNonce
        if not self.security_policy.server_certificate:
            self.security_policy.server_certificate = response.ServerCertificate
        elif self.security_policy.server_certificate != response.ServerCertificate:
            raise ua.UaError("Server certificate mismatch")
        # remember PolicyId's: we will use them in activate_session()
        ep = Client.find_endpoint(response.ServerEndpoints, self.security_policy.Mode, self.security_policy.URI)
        self._policy_ids = ep.UserIdentityTokens
        if self.session_timeout != response.RevisedSessionTimeout:
            _logger.warning("Requested session timeout to be %dms, got %dms instead",
                                self.secure_channel_timeout,
                                response.RevisedSessionTimeout)
            self.session_timeout = response.RevisedSessionTimeout
        self.keepalive = KeepAlive(
            self, min(self.session_timeout, self.secure_channel_timeout) * 0.7)  # 0.7 is from spec
        self.keepalive.start()
        return response



    def server_policy_id(self, token_type, default):
        """
        Find PolicyId of server's UserTokenPolicy by token_type.
        Return default if there's no matching UserTokenPolicy.
        """
        for policy in self._policy_ids:
            if policy.TokenType == token_type:
                return policy.PolicyId
        return default



    def server_policy_uri(self, token_type):
        """
        Find SecurityPolicyUri of server's UserTokenPolicy by token_type.
        If SecurityPolicyUri is empty, use default SecurityPolicyUri
        of the endpoint
        """
        for policy in self._policy_ids:
            if policy.TokenType == token_type:
                if policy.SecurityPolicyUri:
                    return policy.SecurityPolicyUri
                else:   # empty URI means "use this endpoint's policy URI"
                    return self.security_policy.URI
        return self.security_policy.URI



    def activate_session(self, username=None, password=None, certificate=None):
        """
        Activate session using either username and password or private_key
        """
        params = ua.ActivateSessionParameters()
        challenge = b""
        if self.security_policy.server_certificate is not None:
            challenge += self.security_policy.server_certificate
        if self._server_nonce is not None:
            challenge += self._server_nonce

        if self.security_policy.AsymmetricSignatureURI:
            params.ClientSignature.Algorithm = (
                self.security_policy.AsymmetricSignatureURI
            )
        else:
            params.ClientSignature.Algorithm = (
                security_policies.SecurityPolicyBasic256.AsymmetricSignatureURI
            )
        params.ClientSignature.Signature = self.security_policy.asymmetric_cryptography.signature(challenge)
        params.LocaleIds.append("en")
        if not username and not certificate:
            self._add_anonymous_auth(params)
        elif certificate:
            self._add_certificate_auth(params, certificate, challenge)
        else:
            self._add_user_auth(params, username, password)
        return self.uaclient.activate_session(params)


    def _add_anonymous_auth(self, params):
        params.UserIdentityToken = ua.AnonymousIdentityToken()
        params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Anonymous, "anonymous")

    def _add_certificate_auth(self, params, certificate, challenge):
        params.UserIdentityToken = ua.X509IdentityToken()
        params.UserIdentityToken.CertificateData = uacrypto.der_from_x509(certificate)
        # specs part 4, 5.6.3.1: the data to sign is created by appending
        # the last serverNonce to the serverCertificate
        params.UserTokenSignature = ua.SignatureData()
        if certificate.signature_hash_algorithm.name == "sha256":
            params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Certificate, "certificate_basic256sha256")
            sig = uacrypto.sign_sha256(self.user_private_key, challenge)
            params.UserTokenSignature.Algorithm = "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
            params.UserTokenSignature.Signature = sig
        else:
            params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Certificate, "certificate_basic256")
            sig = uacrypto.sign_sha1(self.user_private_key, challenge)
            params.UserTokenSignature.Algorithm = "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
            params.UserTokenSignature.Signature = sig

    def _add_user_auth(self, params, username, password):
        params.UserIdentityToken = ua.UserNameIdentityToken()
        params.UserIdentityToken.UserName = username
        policy_uri = self.server_policy_uri(ua.UserTokenType.UserName)
        if not policy_uri or policy_uri == security_policies.POLICY_NONE_URI:
            # see specs part 4, 7.36.3: if the token is NOT encrypted,
            # then the password only contains UTF-8 encoded password
            # and EncryptionAlgorithm is null
            if self._password:
                _logger.warning("Sending plain-text password")
                params.UserIdentityToken.Password = password.encode('utf8')
            params.UserIdentityToken.EncryptionAlgorithm = None
        elif self._password:
            data, uri = self._encrypt_password(password, policy_uri)
            params.UserIdentityToken.Password = data
            params.UserIdentityToken.EncryptionAlgorithm = uri
        params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.UserName, "username_basic256")

    def _encrypt_password(self, password, policy_uri):
        pubkey = uacrypto.x509_from_der(self.security_policy.server_certificate).public_key()
        # see specs part 4, 7.36.3: if the token is encrypted, password
        # shall be converted to UTF-8 and serialized with server nonce
        passwd = password.encode("utf8")
        if self._server_nonce is not None:
            passwd += self._server_nonce
        etoken = ua.ua_binary.Primitives.Bytes.pack(passwd)
        data, uri = security_policies.encrypt_asymmetric(pubkey, etoken, policy_uri)
        return data, uri


    def close_session(self):
        """
        Close session
        """
        if self.keepalive and self.keepalive.is_alive():
            self.keepalive.stop()
            self.keepalive.join()
        return self.uaclient.close_session(True)



    def get_root_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.RootFolder))



    def get_objects_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.ObjectsFolder))



    def get_server_node(self):
        return self.get_node(ua.FourByteNodeId(ua.ObjectIds.Server))



    def get_node(self, nodeid):
        """
        Get node using NodeId object or a string representing a NodeId
        """
        return Node(self.uaclient, nodeid)



    def create_subscription(self, period, handler):
        """
        Create a subscription.
        returns a Subscription object which allow
        to subscribe to events or data on server
        handler argument is a class with data_change and/or event methods.
        period argument is either a publishing interval in milliseconds or a
        CreateSubscriptionParameters instance. The second option should be used,
        if the opcua-server has problems with the default options.
        These methods will be called when notfication from server are received.
        See example-client.py.
        Do not do expensive/slow or network operation from these methods
        since they are called directly from receiving thread. This is a design choice,
        start another thread if you need to do such a thing.
        """

        if isinstance(period, ua.CreateSubscriptionParameters):
            return Subscription(self.uaclient, period, handler)
        params = ua.CreateSubscriptionParameters()
        params.RequestedPublishingInterval = period
        params.RequestedLifetimeCount = 10000
        params.RequestedMaxKeepAliveCount = 3000
        params.MaxNotificationsPerPublish = 10000
        params.PublishingEnabled = True
        params.Priority = 0
        return Subscription(self.uaclient, params, handler)



    def reconciliate_subscription(self, subscription):
        """
        Reconciliate the server state with the client
        """
        node = self.get_node(
            ua.FourByteNodeId(ua.ObjectIds.Server)
        )
        # returns server and client handles
        monitored_items = node.call_method(
            ua.uatypes.QualifiedName("GetMonitoredItems"),
            ua.Variant(subscription.subscription_id, ua.VariantType.UInt32)
        )
        return subscription.reconciliate(monitored_items)



    def get_namespace_array(self):
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        return ns_node.get_value()



    def get_namespace_index(self, uri):
        uries = self.get_namespace_array()
        return uries.index(uri)



    def delete_nodes(self, nodes, recursive=False):
        return delete_nodes(self.uaclient, nodes, recursive)



    def import_xml(self, path=None, xmlstring=None):
        """
        Import nodes defined in xml
        """
        importer = XmlImporter(self)
        return importer.import_xml(path, xmlstring)



    def export_xml(self, nodes, path):
        """
        Export defined nodes to xml
        """
        exp = XmlExporter(self)
        exp.build_etree(nodes)
        return exp.write_xml(path)



    def register_namespace(self, uri):
        """
        Register a new namespace. Nodes should in custom namespace, not 0.
        This method is mainly implemented for symetry with server
        """
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        uries = ns_node.get_value()
        if uri in uries:
            return uries.index(uri)
        uries.append(uri)
        ns_node.set_value(uries)
        return len(uries) - 1



    def load_type_definitions(self, nodes=None):
        """
        Load custom types (custom structures/extension objects) definition from server
        Generate Python classes for custom structures/extension objects defined in server
        These classes will available in ua module
        """
        return load_type_definitions(self, nodes)



    def load_enums(self):
        """
        generate Python enums for custom enums on server.
        This enums will be available in ua module
        """
        return load_enums(self)



    def register_nodes(self, nodes):
        """
        Register nodes for faster read and write access (if supported by server)
        Rmw: This call modifies the nodeid of the nodes, the original nodeid is
        available as node.basenodeid
        """
        nodeids = [node.nodeid for node in nodes]
        nodeids = self.uaclient.register_nodes(nodeids)
        for node, nodeid in zip(nodes, nodeids):
            node.basenodeid = node.nodeid
            node.nodeid = nodeid
        return nodes



    def unregister_nodes(self, nodes):
        """
        Unregister nodes
        """
        nodeids = [node.nodeid for node in nodes]
        self.uaclient.unregister_nodes(nodeids)
        for node in nodes:
            node.nodeid = node.basenodeid
            node.basenodeid = None



    def get_values(self, nodes):
        """
        Read the value of multiple nodes in one roundtrip.
        """

        nodes = [node.nodeid for node in nodes]
        results = self.uaclient.get_attributes(nodes, ua.AttributeIds.Value)
        return [result.Value.Value for result in results]



    def set_values(self, nodes, values):
        """
        Write values to multiple nodes in one ua call
        """
        nodeids = [node.nodeid for node in nodes]
        dvs = [ua_utils.value_to_datavalue(val) for val in values]
        results = self.uaclient.set_attributes(nodeids, dvs, ua.AttributeIds.value)
        print(results)
        for result in results:
            result.check()

    def set_values1(self, nodes, values):
        """
        Write values to multiple nodes in one ua call
        """
        dv = ua.DataValue(ua.Variant(values[0], ua.VariantType.Boolean))
        for node in nodes:
           node.set_value(dv)
    # def ProcessTrigger(self):
    #     while True:
    #         if(tempQue.empty()):
    #            continue
    #         proxy = tempQue.get()
    #         # print(proxy)
    #         for p in proxy:
    #             print(p)
    #
    #         # chat.server.invoke("send", "Raspi",proxy )#+ ",Tm#"+tempstr)

c1Indx = None
c2Indx = None
sIndx = None
eIndx = None

global calconfig
calconfig = None
def reset(client, node ):
    global c1Indx
    global c2Indx
    global sIndx
    global eIndx

    try:
        var = client.get_node(ua.NodeId(node, 4))
        dv = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))
        var.set_value(dv)
        print(var.get_value())
        time.sleep(1)

        dv = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))
        var.set_value(dv)
        print(var.get_value())
        if node == 616:
            print("Index Reset")
            c1Indx = 0
            c2Indx = 0
            sIndx = 0
            eIndx = 0
    except:
        print(sys.exc_info()[1])

def server():
    global calconfig
    print("Connecting UA Server")
    client = Client("opc.tcp://192.168.1.2:4840",4)
    client.connect()
    client.get_endpoints()

    print("Connected ... ")
    reset(client, 616)
    print("Train end")
    #  Load Temp. Calibration
    with open('Calibration.json') as f:
        calconfig = json.load(f)
    for i in range(1,5):
        s = str(i)
        print(calconfig["tempMin"+s])
        print(calconfig["tempMax"+s])
        print(calconfig["cntMin"+s])
        print(calconfig["cntMax"+s])
         
    return client


def SendSignal(client,chat,tempQue):
    global c1Indx
    global c2Indx
    global sIndx
    global eIndx
    C1nodes = []
    C2nodes = []
    Snodes = []
    Enodes = []
    c1Indx = 0
    c2Indx = 0
    sIndx = 0
    eIndx = 0



    # values =[]
    # values.append(ua.Variant([""], ua.VariantType.String))


    for i in range(205, 404):
        Snodes.append(client.get_node(ua.NodeId(i, 4)))

    for i in range(4, 203):
        C1nodes.append(client.get_node(ua.NodeId(i, 4)))

    for i in range(618, 817):
        C2nodes.append(client.get_node(ua.NodeId(i, 4)))
    for i in range(406 , 605):
        Enodes.append(client.get_node(ua.NodeId(i, 4)))
    startTrain = client.get_node(ua.NodeId(829, 4))
    while True:
        # print(Snodes[0 :10])
        # print(c1Indx)
        if startTrain.get_value() == False:
            time.sleep(1.0)
            continue
        try:
            tmp =ReadAxle(client, Snodes[sIndx :(sIndx + 10)], tempQue , sIndx)
            if  tmp>-1:
                sIndx = tmp
            tmp = ReadAxle(client, C1nodes[c1Indx :(c1Indx + 10)], tempQue ,c1Indx)
            if  tmp>-1:
                c1Indx = tmp

            tmp = ReadAxle(client, C2nodes[c2Indx : (c2Indx + 10)], tempQue,c2Indx)
            if  tmp>-1:
                c2Indx = tmp
            tmp = ReadAxle(client, Enodes[eIndx :(eIndx + 10)], tempQue,eIndx)
            if  tmp>-1:
                eIndx = tmp
            # tempQue.put(plcData)
            time.sleep(0.01)
        except :
            print("PLC read error")

def removeEmpty(test_list):
    res = []
    for ele in test_list:
        if ele != "":
            res.append(ele)
    return  res
def GetcalTemp(s, strTemp):
    global calconfig
    #print(calconfig)
    tempMin=  calconfig["tempMin"+s]
    tempMax = calconfig["tempMax"+s]
    cntMin = calconfig["cntMin"+s]
    cntMax = calconfig["cntMax"+s]

    value = int(strTemp)
    lmtRatio = (tempMax - tempMin);
    orgRatio = (cntMax - cntMin);
    v = (lmtRatio * (value - cntMin) / orgRatio) + tempMin;

    # value = int(strTemp)
    # lmtRatio = (105.00 - 32.00);
    # orgRatio = (3218 - 1019);
    # v = (lmtRatio * (value - 1019) / orgRatio) + 27.00;
    return   str(v);
def ReadAxle(client, nodes, tempQue , indx):
   # print(nodes, indx)
    if(len(nodes) == 0 ):
        return 0
    try:
        plcData = client.get_values(nodes)
        cnt = 0
        # print( plcData)
        for p in plcData:
            if (p != ""):
                print(p)
                d = p.split(',')
                # dtime = d[2].split(" ")
                # tempstr = ""
                # tempstr = tempstr + d[0] + "-" + d[1] + "-" + dtime[0] + "/" + str(datetime.today().month) + "/" + str(
                #     datetime.today().year) + "/" + dtime[1] + ":" + dtime[2] + ":" + dtime[3] + ":" + dtime[4] + ":" + \
                #           dtime[5]

                    # d = s.split(',')
                tm = d[0]+"$" + d[1].strip("     ") + "$"
                tt = removeEmpty(d[2].split(" "))
                # print(tt)
                # tt = d[2].strip('')
                # tt = tt.split("  ")
                # print(tt[5])
                ms = float( tt[3]) + (int(tt[4]) / 1_000_000_000.0);

                tempstr = tm + str(datetime.today().year) + "/" + str(datetime.today().month) + "/" + tt[0] + "  " + tt[1] + ":" + tt[2]  + ":" + str( ms)

                if "C1" in d[0] or "C2" in d[0] :
                    tempstr = tempstr +"#" +  GetcalTemp("1",d[3])+"," +  GetcalTemp("2",d[4])+"," +  GetcalTemp("3",d[5])+"," +  GetcalTemp("4",d[6])

                tempQue.put(tempstr)
                #print("Raspi:"+tempstr)
                cnt = cnt + 1


        if (indx + cnt  >=  199):
            print("Reach to 200")
            return  0
        else:
            return  (indx +cnt)
        return indx
    except :
        print("Error reading ",sys.exc_info()[1])
        return indx + cnt



def startThread(client , Chat , tmp):
    tmpr = Thread(target= SendSignal, args=(client, Chat,tmp))
    tmpr.daemon = True
    tmpr.start()



def GetHBDreply(client):
    while True:
        if "HBD:e" in input():
            print("Terminating train...")
            reset(client, 616)
            print('Train End')
            #time.sleep(2)

# client=server()
# startThread(client,None,tempQue)
#
# tmpr1 = Thread(target=GetHBDreply, args = (client,))
# tmpr1.daemon = True
# tmpr1.start()
# s= "C1,     1,  17  18  27  28  789350000,  3208,  3139,  2894,  2325,"
#
# d = s.split(',')
# print(removeEmpty(d[2].split(' ')))
# tm = "C$"+d[1].strip("     ") +"$"
# tt = d[2].strip('')
# tt = tt.split("  ")
# # ms = str(int(tt [5]) / 1000.0)
# ms = str(int(tt [5]) / 1_000_000_000.0);
# print(tm + str( datetime.today().year) + "/"+str( datetime.today().month) + "/"+ tt [1] + " " +tt [2] + ":" +tt [3]+ ":" +tt [4] + " " + ms )
# print(tm)
# SendSignal(None , None , None)

# if __name__ == "__main__":
#     # creating processes
#     # tempQue = queue.Queue(maxsize=1000)
#
#     # p1 = multiprocessing.Process(target=chat1.main, )
#     #
#     # p2 = multiprocessing.Process(target=server, )
#     #
#     # # starting process 1
#     # p1.start()
#     # time.sleep(2)
#     # # starting process 2
#     # p2.start()
#     #
#     # # wait until process 1 is finished
#     # p1.join()
#     # # wait until process 2 is finished
#     # p2.join()
#     # #
#     # # # both processes finished
#     # print("Done!")
#
#
#     #
#     tmpr = Thread(target=chat1.main,)
#     tmpr.start()
#
#     time.sleep(10)
#     tmprsvr = Thread(target=server,)
#     tmprsvr.start()
#
#     time.sleep(10)
#     tmpr1 = Thread(target=chat1.GetTemptr)
#     tmpr1.start()



