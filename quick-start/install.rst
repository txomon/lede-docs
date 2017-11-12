Installation
============

There are several installation methods documented in this quick guide depending on the following:
  * If your device still has the vendor firmware, follow the `Factory installation` procedure.
  * If your device already has an older LEDE or OpenWrt firmware on it, follow the `Sysupgrade` procedure.

    * If your current LEDE installation does not have the web admin GUI installed or if you prefer to upgrade from the command line (upgrade from command line provides more fine-grained control), refer to :doc:`Upgrading LEDE from the Command Line </user-guide/sysupgrade-cli>`.

  * If you have any questions about this distinction, ask for help on the `Installing and Using LEDE forum section <https://forum.lede-project.org/c/installation>`_ before beginning.


Device selection
----------------

Devices with >=8 MBytes Flash memory and >=64 MBytes RAM allow a full-featured LEDE installation with GUI.

Devices with 4 MByte or less Flash memory can install LEDE as well, but with a limited feature set. They cannot use optional packages and in some cases may also not have a web GUI, due to limited flash space and may therefore have to stick to command line administration only. The creation of individual custom packages may help to avoid some of these limitations on such 'small' devices, but such a custom-package-creation is not part of this howto.

If you want to purchase a new router for LEDE, stick to devices with >=8 MBytes Flash memory and >=64 MBytes RAM.


Locate and download the LEDE firmware
-------------------------------------

On the `Table of Hardware: Firmware downloads <toh_fwdownload>`_ page, locate your specific device. The table of hardware only references stable release versions of LEDE. If you are a newbee, only use these stable release version for first-time device installations; do not initially use a (clearly marked) develop/snapshot version downloaded from other subfolders. This ensures that you get the easiest possible first-time LEDE installation experience.

When you have located your device in this list, click on the "View/edit data" link of the device record. This will open a new page with several details for your specific device. We recommend to bookmark that page, as it has lots of helpful information about your router.

Factory install
'''''''''''''''

On this device-specific **Techdata** page, at the bottom locate the line called **"Firmware LEDE Install URL"** that links to a downloadable file called **"...factory.bin"** file.

Sysupgrade
''''''''''

On this device-specific **Techdata** page, at the bottom locate the line called **"Firmware LEDE Upgrade URL"** that links to a downloadable file called **"...sysupgrade.bin"** file.


Download Troubleshooting
''''''''''''''''''''''''

The LEDE download directory structure matches the OpenWrt download directories.

If the Standard Flashing Instructions don't provide the information you're looking for, ask on the `Installation Category of the forum <https://forum.lede-project.org/c/installation>`_ or search the OpenWrt site for enough information about your device to find the proper LEDE firmware image.

Find the **Device Page** for your device on the **OpenWrt Table of Hardware** at https://wiki.openwrt.org/toh/start

Find the name and URL of the proper OpenWrt firmware image (factory or sysupgrade).

Then go to `downloads.lede-project.org <https://downloads.lede-project.org/snapshots/targets/>`_ and find the LEDE image from the corresponding directory.

Follow the flashing instructions on the **OpenWrt Device Page**, if needed.


I still cannot find the specified file
++++++++++++++++++++++++++++++++++++++

Some devices lack an easy installable image and require a special (and usually a bit more complex) installation procedure that is device-specific. This tutorial won't apply for such devices. If you have such a device, locate the corresponding device page in the older OpenWrt wiki and follow the custom installation description (Eventually older OpenWrt info will be migrated to the LEDE tech data pages).

If you can't find your device in the Table of Hardware, or if there is not the file you are looking for, you can consult the `"Installing and Using LEDE" Forum <https://forum.lede-project.org/c/installation>`_ for help.


I am in a folder with my device name in multiple files
++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you have accidentally browsed the generic LEDE download folders to locate your device, you might see some more download files matching your device. Ignore those other files for your device: you only want the specified file.


Verify the downloaded firmware file
-----------------------------------

This step is to verify a downloaded firmware binary against a reference checksum to avoid download errors.

This ensures that you have a 100% correct download and that you will not brick your device by applying a faulty download.

.. warning:: Only continue with flashing if the firmware checksum of your download matches the checksum stated on the download site!


Get the reference checksum
''''''''''''''''''''''''''

Obtaining the reference checksum from the download page is currently a little inconvenient, as the reference checksums of the firmware binaries are currently not listed on the LEDE device tech data pages.

To get the reference checksum, recall the URL path of firmware binary you just downloaded, e.g. if your firmware download-URL was https://downloads.lede-project.org/releases/version/targets/chipset/modell/lede-something-something-something-something-something.bin
then open the web page https://downloads.lede-project.org/releases/version/targets/chipset/modell/

There you will find a list of firmware images, one of it being the file you just downloaded. Now note the additional checksum string on the right side of the download link (in the table column "sha256sum").

We will now calculate a checksum of the downloaded file and compare it with that string. If that check fails, the firmware file was not properly downloaded and if you proceed flashing such a file, you will probably brick the device permanently or require annoying procedures to recover.

.. warning:: On checksum mismatches, download the firmware file again and compare it again. If the checksum is still wrong in repeated attempts, ask the `LEDE forums <https://forum.lede-project.org/c/installation>`_ for help.


Calculate the checksum of the downloaded file
'''''''''''''''''''''''''''''''''''''''''''''


Calculating checksum on Windows
+++++++++++++++++++++++++++++++

Newer Windows has a built-in tool to calculate sha256sums called 'certutil', but it has no graphical user interface so we will have to use the command line to interact with it.

Older Windows version need to download a sha256 tool, for example `MD5 & SHA Checksum Utility <https://raylin.wordpress.com/downloads/md5-sha-1-checksum-utility>`_ (the free version).

To use the built-in certutil, click the Windows icon, type "cmd" and hit enter.

Execute (assuming you downloaded the file to your Downloads folder)::

   certutil -hashfile "%USERPROFILE%/Downloads/LEDE-file-name-here" sha256

This will print a checksum like this (file name followed by string with letters and numbers)::

   SHA256-Hash of file C:\Users\USERNAME\Downloads\lede-17.01.1-...-factory.bin:
   79 f9 4e fa d3 2c 14 8f f1 95 3f 09 6d 98 c7 41 c0 ff 8f 7e b4 68 8c 9d 5b f9 fb 01 c0 90 fb ab

Remove spaces from this checksum output (e.g. using replace function in notepad)::

   79f94efad32c148ff1953f096d98c741c0ff8f7eb4688c9d5bf9fb01c090fbab

Check that the checksum string without blanks matches the one you can find in the **sha256sums** field on the download page.


Calculating checksum on Mac
+++++++++++++++++++++++++++

Mac has an integrated tool to check sha256sums, but it has no graphical user interface so we will have to use the Terminal to interact with it.

Click the Finder icon in the Dock.

Click Applications in the Favorites list.

Find the Utilities folder and click to open it.

Locate Terminal and double-click the icon to open the program.

Open a terminal window, and execute (assuming you downloaded the file on the desktop)::

   shasum -a 256 ./Desktop/file-name-here

it will print something like this (string with letters and numbers followed by file name)::

   bba93584fc44045629888e6b147851917cd0c83fcc91a7e6dbe90bdce76 -17.01.0-...-sysupgrade.bin

Check that the checksum string matches the one you can find in the **sha256sums** field on the download page.


Calculating checksum on Linux
+++++++++++++++++++++++++++++

Linux has an integrated tool that is accessible from command line, similar to Mac.

Some file managers (dolphin and other more powerful ones used in KDE user interface) offer this functionality in the file property window (right-click on the file, select Properties, click on "Checksums" tab, that tab appears only for binary files, like firmware images). It will offer buttons to calculate the SHA256sum and a field where you can paste the SHA256 string from sha256sums file to verify that it is correct.

If your file manager does not offer any of this, you can always use the terminal window and type in the following command (again assuming you downloaded the file on the desktop)

Command line verification:

On the terminal window, execute::

   sha256sum ./Desktop/file-name-here

This will print something like this::

   1a7c8bba93584fc44045629888e6b147851917cd0c83fcc91a7e6dbe90bdce76 lede-17.01.0-...-sysupgrade.bin

Check that the checksum string matches as the one you can find in the **sha256sums** field on the download page.


Troubleshooting
'''''''''''''''


Checksum is not the same
++++++++++++++++++++++++

If the checksum process has reported a checksum mismatch, do NOT start flashing, as the download could be corrupt. A corrupt firmware file can brick your device! Instead retry with another download attempt and retry the checksum step.


Checksum is still not the same
++++++++++++++++++++++++++++++

If the checksum step fails repeatedly, you can consult the `"Installing and Using LEDE" Forum <https://forum.lede-project.org/c/installation>`_ for help. Be sure to include the exact brand, model, and version of your device.


Flash the firmware
------------------


Factory install
'''''''''''''''

Connect to the device via Ethernet cable (Only fallback to wireless, if the device has no Ethernet connection options)

Ensure that the LEDE firmware file that you are about to flash, matches your router model and is called **"....factory.bin"**, as you will use it to modify a vendor's **factory** firmware towards LEDE.

 Log into the device's admin web interface and locate the device-specific firmware installation function. Follow the device-specific instructions of your manufacturer's user guide for installing firmware and use this to install the  "...factory.bin" firmware file of LEDE.

Wait while the device writes the firmware image to its flash memory. This can take several minutes (the Device Page may state an expected time for this process). At the end, the device will reboot automatically.

The new firmware has been installed. Continue with the next section to check the result.


Sysupgrade
''''''''''

If you want to preserve your existing LEDE configuration, backup the configuration before flashing, by using the web admin GUI menu: (LEDE default IP: http://192.168.1.1) -> **System > Backup/flash firmware** -> **Backup/Restore section** > **Generate archive**.

If you do not choose to backup, the existing LEDE configuration will be lost and you have to start with a default LEDE configuration after the upgrade.

If you have NAS storage attached to your LEDE device, decide by yourself, whether you require a backup of files on that NAS.

The backup includes config files of manually installed packages but not the packages themselves. After flashing the firmware you will need to install those packages again.


Verify firmware file and flash the firmware
+++++++++++++++++++++++++++++++++++++++++++

Connect to the device via Ethernet cable (Use wireless only, if the device has no Ethernet connection options)

Log into the LEDE's web admin GUI and in the **System -> Backup/Flash Firmware** menu, go to the "Flash new firmware image" section.

**Uncheck**/clear the **"Keep settings"** checkbox**!** (more info regarding the "`Keep settings checkbox"` and it's rare use cases).

Ensure that the LEDE firmware file you are about to flash matches your router model and is called **"....sysupgrade.bin"**, as you will **upgrade** an existing LEDE/OpenWrt system towards a newer LEDE firmware version.

In the **"Flash new firmware image"** section, click **"Choose file"** to select the image file, then click "Flash image...". This displays a “Flash Firmware - Verify" page, containing a SHA256 checksum of the image file just uploaded to the router.

Check that the firmware-checksum displayed on the web GUI matches the SHA256 checksum from the LEDE downloaded page. If it does not match, do NOT continue, as it is a corrupt file and will likely brick your device.  Note: If you are upgrading from OpenWRT 15.05, the 32 character displayed is an MD5 checksum, not SHA256.  Please verify this MD5 checksum on your operating system before proceeding.

.. warning:: Careful, this step is as important as the verification of the previous step. Please make sure that the file checksum still matches.

If the checksum matches, click "Proceed". This starts the "System - Flashing ..." along with a spinning wheel and "Waiting for changes to be applied..."

It can take several minutes, while the router uploads the firmware image and write it into its flash ROM and finally reboots.

The new firmware has been installed. Continue with the next section to check the result.


Keep settings checkbox
++++++++++++++++++++++

The "Keep settings" checkbox is a more advanced feature.

If you do not precisely understand the button's use cases, **uncheck "Keep Settings"** every time you flash a new LEDE sysupgrade to your device, to **not** preserve settings.

  * Only check the "Keep settings" checkbox on minor LEDE->LEDE bug fix upgrades that are known to not change the config structure
  * Only use it for the same firmware channel (release->release, snapshot->snapshot)
  * Checking it will preserve several specific config files on the upgrade, but not the whole overlay partition.
  * If you flash your device regularly, preferably consider unchecking "Keep Settings" every time you flash the router and instead create a custom installation script for your customization. Example: `config-openwrt.sh <https://github.com/richb-hanover/OpenWrtScripts/blob/master/config-openwrt.sh>`_ script.
  * "Keep settings" can also be used to preserve own configurations files. To do, go to **System > Backup/Flash Firmware** and open the **Configuration** tab, add your config filesthere and click "Submit". This will allow you to add your custom configuration files to the ''/etc/sysupgrade.conf'' file that is read by sysupgrade when it is backing up files. Click "Submit" when done editing.\\ To view all files that would be kept when "keep settings" is checked, click the "**Open list...**" button.


Next steps
----------

From here, we will gain access to the new LEDE firmware, through the different methods, and move into making a basic setup.


Installing LEDE Development Snapshots
-------------------------------------

**For experienced users only!**

The steps below install LEDE development snapshot firmware on your device.

What is a development snapshot firmware?
''''''''''''''''''''''''''''''''''''''''

Development snapshots are also known as simply "snapshots" or the outdated term "trunk builds". Snapshots are versions of LEDE that are "in development". They are rebuilt frequently, often multiple times a day.

I am a standard consumer, do I want a development snapshot firmware?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

**No!** Although they are the latest version, there is no guarantee that any particular snapshot build will be bug-free, or even work at all.\\
Snapshots are not likely to be stable enough to be used on your home router, where you or members of your family rely on the network.\\
As a standard consumer stick to the official release versions of LEDE.

Snapshots do not have LuCi web admin GUI installed by default
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

On snapshots, LuCi has to be installed manually (if needed).

Manual LuCi installation by package may require more free flash storage than a 4MB-flash-device can handle, `see 4/32 device warning <meta:infobox:432_warning>`_

To manually install LuCi: `LuCI installation <user-guide/luci:Essentials>`_

TL;DR: opkg update ; opkg install luci ; /etc/init.d/uhttpd start ; /etc/init.d/uhttpd enable

This should get a working GUI that repsonpds to  http://192.168.1.1 requests by a browser, mind you I did not actually test that...

Installing a LEDE Snapshot
''''''''''''''''''''''''''

To install (or "flash") a LEDE snapshot firmware image, just follow the standard flashing instructions: `Factory install <quick-start:factory_installation>`_ and `Sysupgrade <quick-start/sysupgrade:luci>`_, with the only difference to use it for a firmware file from the snapshot download section.
