/** codec configuration
 * Decode uplink function
 * 
 * @param {object} input
 * @param {number[]} input.bytes Byte array containing the uplink payload, e.g. [255, 230, 255, 0]
 * @param {number} input.fPort Uplink fPort.
 * @param {Record<string, string>} input.variables Object containing the configured device variables.
 * 
 * @returns {{data: object}} Object representing the decoded payload.
 */
function toHexString(bytes) {
    return bytes.map(function(byte) {
        return ("00" + (byte & 0xFF).toString(16)).slice(-2)
      }).join('');
}
function decodeUplink(input) {
 var tohex = toHexString(input.bytes);
  return {
    data: {mydata:tohex}
  };
}

/**
 * Encode downlink function.
 * 
 * @param {object} input
 * @param {object} input.data Object representing the payload that must be encoded.
 * @param {Record<string, string>} input.variables Object containing the configured device variables.
 * 
 * @returns {{bytes: number[]}} Byte array containing the downlink payload.
 */
function encodeDownlink(input) {
  return {
    bytes: []
  };
}
