

Step 1: Set Up NTP Server on Windows 10
Enable NTP Server:

Press Win + R, type regedit, and press Enter to open the Registry Editor.
Navigate to the following path:
sql
Copy code
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpServer
Find the Enabled key and set its value to 1.
Configure NTP Server:

Still in the Registry Editor, navigate to:
sql
Copy code
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config
Find the AnnounceFlags key and set its value to 5.
Open Command Prompt as Administrator:

Press Win + X and select Command Prompt (Admin) or Windows PowerShell (Admin).
Restart Windows Time service:

sh
Copy code
net stop w32time
net start w32time
Step 2: Configure Jetson Nano to Sync Time with Windows 10 PC
Install NTP client:

sh
Copy code
sudo apt-get update
sudo apt-get install ntpdate
Configure NTP client:

Open the NTP configuration file:
sh
Copy code
sudo nano /etc/ntp.conf
Add the IP address of your Windows 10 PC as the NTP server:
sh
Copy code
server 192.168.1.100
Replace 192.168.1.100 with the IP address of your Windows 10 PC.
Update NTP configuration:

sh
Copy code
sudo systemctl restart ntp
Synchronize time manually (optional):

sh
Copy code
sudo ntpdate 192.168.1.100
Step 3: Verify Time Synchronization
On Jetson Nano:

Check the NTP synchronization status:
sh
Copy code
ntpq -p
You should see the IP address of your Windows 10 PC listed as a server.
On Windows 10 PC:

Verify that the Windows Time service is running correctly:
sh
Copy code
w32tm /query /status





Create a New Inbound Rule:

Go to Advanced Settings.
Right-click on Inbound Rules and select New Rule.
Select Port and click Next.
Choose UDP and specify port 123, then click Next.
Select Allow the connection, then click Next.
Ensure all profiles are checked, then click Next.
Name the rule (e.g., NTP UDP 123) and click Finish.

Restart Windows Time Service:

sh
Copy code
net stop w32time
net start w32time

 Retry Time Synchronization on Jetson Nano
Manually Synchronize Time:
sh
Copy code
sudo ntpdate -u 192.168.1.15
The -u option tells ntpdate to use an unprivileged port.

cronjob
*/1 * * * * /home/jetson/Mvis_Jetson_Nano_Project/timesync.sh