====== LEDE Starter FAQ ======

**Ok, so I've successfully flashed LEDE on my device. what should I do next?**\\
Set an initial root password, setup WiFi, get familiar with the troubleshooting/rescue options in the user guide, then browse the user guide for further config you may be interested in.

**How do I access the web admin GUI on a default installation?**\\
Open http://192.168.1.1 or http://lede in your favorite web browser

**What is the default admin username in LEDE?**\\
"root"

**What is the initial password for root?**\\
There is no initial password set. Please set one manually, after your first login, either by using ''passwd'' on the command line or in [[http://lede/cgi-bin/luci/admin/system/admin| LUCI Menu System/Administration]]

**Can I reset the 'root' password, in case I have forgotten it?**\\
Yes, check the troubleshooting section of the user guide.

**I seem to have messed up the LEDE device configuration, my LEDE device is no longer accessible. What do I do?**\\
Check the troubleshooting section of the user guide, several recovery options are available.

**How can I enable SSL for the web admin gui?**\\
In an SSH-command line, run ''opkg update'', then install the package ''opkg install luci-ssl'', then restart the router. Then you can access https://192.168.1.1 or https://lede with your favorite web browser

**Is there a command line editor available in SSH?**\\
use ''vi''. It's most important key shortcuts are:\\
|ESC :q! | exits without saving|
|ESC :wq | exit and save|
|ESC i | insert text at the current cursor position|
|ESC x | delete the character under the cursor|
|ESC dd | delete the whole current line|
|ESC o | open new line below cursor|
|ESC O | open new line above cursor|

**What other tools can I use for administration of LEDE from a windows client?**\\
Get [[http://www.putty.org|Putty]] for SSH access to LEDE and get [[https://winscp.net|WinSCP]] as a file browser. For WinSCP to connect successful, you have to first ''opkg update'' then install the package ''opkg install openssh-sftp-server''. You can then use WinSCP to click through the LEDE file system and use its GUI editor for editing LEDE config files.

**I would like to customize LEDE, but am having difficulties finding the packages that I am interested in.**\\
Remember to first run ''opkg update'' once after each LEDE reboot, to refresh the list of available packages. LEDE will only temporary store the retrieved list in a temp RAM filesystem, losing the list of updates on every reboot.

**Why is there a "WAN" and a "WAN6" and a "LAN" interface in LEDE, but no "LAN6" ?**\\
Note that there is a "WAN" and "WAN6" interface. Each of the 2 WAN interfaces holds config data related to the upstream interface (WAN is for IPv4 and has "DHCP client", while WAN6 is for IPv6 has "DHCPv6 client"). On the other hand "LAN" has both the config data for the downstream side for both IPv4 and IPv6 associated, so there is no need to have an extra LAN6 interface.
Also note that both an interface and a zone called "LAN" exist. Also "WAN" is used both as a name for a zone and as a name for the IPv4 WAN interface. Both the "WAN" and "WAN6" interface belong to the "WAN" zone (so furthermore there is no "WAN6" zone)

**Why is there both a "Save & Apply" and a "Save" button in LuCi?**\\
You can do several different changes in different tabs, each time clicking "Save" without committing the changes. You can then use "Save & Apply" to commit all of those changes in one transaction.

**What is the difference of total available memory, free and buffered shown in LuCi status overview?**\\
Total = free + buffered. \\
Buffered = memory that is temporarily in use to handle I/O operations\\
Free = really free memory\\

