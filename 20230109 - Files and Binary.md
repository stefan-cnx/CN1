Welcome to our CN1 Class
========================
9th January 2023 13:00

YOU CAN ACCESS THIS FILE @: https://raw.githubusercontent.com/stefan-cnx/CN1/main/20230109%20-%20Files%20and%20Binary.md

First Task:
-----------
1. Create a text file.
2. Include following text into the text file:
   "HELLO WORLD,
    we love the sun."
3. How large is this text file? Explain!
4. What is the binary representation of this file?
   (Use binary or hex notation for step 4.)


Second Task:
------------

Look up the Windows Commands below:

color
dir
cd
copy
start https://google.com/
echo
pause
ipconfig
ipconfig /all
ipconfig /all | findstr DNS
ipconfig /release
ipconfig /renew (use release before renew)
ipconfig /release “Wi-Fi”
ipconfig /displaydns
ipconfig /displaydns | clip    (copies output to the clipboard)
ipconfig /flushdns
nslookup mycourseresource.com
nslookup mycourseresource.com 8.8.4.4
nslookup -type=mx mycourseresource.com
nslookup -type=mx mycourseresource.com 8.8.4.4
nslookup -type=txt mycourseresource.com
nslookup -type=ptr mycourseresource.com (pointer)
cls
getmac /v
powercfg /energy   (requires admin) copy report path and paste into command line to open
powercfg /batteryreport
assoc
assoc .mp4=VLC.vlc
chkdsk /f
chkdsk /r
sfc /scannow
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth => finish up by running sfc /scannow
tasklist | findstr chrome
taskkill /f /pid xxxxx
netsh wlan show wlanreport
netsh interface show interface
netsh interface ip show address | findstr “IP Address”
netsh interface ip show dnsservers
netsh advfirewall set allprofiles state off
netsh advfirewall set allprofiles state on
ping mycourseresource.com
ping -t mycourseresource.com  (Ctrl + C to stop)
tracert mycourseresource.com
tracert -d mycourseresource.com   (faster without resolving …)
netstat 
netstat -af   (0.0.0.0 = every single IP address listening and waiting for connection)
netstat -o     (all open (established) connections)
netstat -e -t 5
route print   (prints the computers routing table)
route add 192.168.1.0 mask 255.255.255.0 192.168.0.0
route delete 192.168.1.0
shutdown /r /fw /f /t 0   (reboots into BIOS)

Third Task:
-----------
@ECHO OFF 
ECHO Welcome to this batch file
ECHO Have a good day
PAUSE

ECHO Please wait... Checking system information.

ECHO ============================================
ECHO WINDOWS INFO
ECHO ============================================
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
systeminfo | findstr /c:"System Type"
:: Section 2: Hardware information.
ECHO ============================================
ECHO HARDWARE INFO
ECHO ============================================
systeminfo | findstr /c:"Total Physical Memory"
ECHO:
ECHO Motherboard:
wmic baseboard get product,manufacturer,version,serialnumber
ECHO CPU:
wmic cpu get name,serialnumber
ECHO Drive:
wmic diskdrive get name,model,size
ECHO Video:
wmic path win32_videocontroller get name
:: Section 3: Networking information.
ECHO ============================================
ECHO NETWORK INFO
ECHO ============================================
ipconfig | findstr IPv4
ipconfig | findstr IPv6
PAUSE


