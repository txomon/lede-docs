Sysupgrading an existing LEDE device from the web admin GUI
===========================================================

Your device must already have an older LEDE or OpenWrt firmware installed, to be eligible for this "sysupgrade" procedure.

  * Alternatively refer to the :doc:`factory installation <factory-installation>` howto, to install LEDE on a device that still has vendor factory firmware on it.
  * If your current LEDE installation does not have the web admin GUI installed or if you prefer to upgrade from the command line (upgrade from command line provides more fine-grained control), refer to :doc:`Upgrading LEDE from the Command Line </user-guide/sysupgrade.cli>`.
  * If you have any questions about this description, ask for help on the `Installing and Using LEDE forum section <https://forum.lede-project.org/c/installation`_ before beginning.

Locate and download the LEDE firmware
-------------------------------------

  - On the :doc:`Table of Hardware: Firmware downloads </toh/views/toh_fwdownload>` page, locate your specific device.
  - Download the sysupgrade file.

Troubleshooting:
  * Some devices lack a sysupgrade image and require a special (and usually a bit more complex) installation procedure that is device-specific. This tutorial won't apply for such devices. Instead follow the custom installation description on the corresponding device page in the OpenWrt wiki.
  * If you can't find your device, or if there is no "...sysupgrade.bin", you can consult the `"Installing and Using LEDE" Forum <https://forum.lede-project.org/c/installation`_ for help.
  * If you don't find your device in the Table of Hardware or Device Pages/Techdata pages, you can also try :doc:`alternative ways to find LEDE firmware images <alternate-directory-search>`
  * If you have accidently browsed the generic LEDE download folders to locate your device, you might see some more download files matching your device. Ignore those files: you only want the "...sysupgrade.bin" file .

Backup
------

  * If you want to preserve your existing LEDE configuration, backup the configuration before flashing, by using the web admin GUI menu: (LEDE default IP: http://192.168.1.1) -> **System > Backup/flash firmware** -> **Backup/Restore section** > **Generate archive**.
  * If you do not choose to backup, the existing LEDE configuration will be lost and you have to start with a default LEDE configuration after the upgrade.
  * If you have NAS storage attached to your LEDE device, decide by yourself, whether you require a backup of files on that NAS.
  * The backup includes config files of manually installed packages but not the packages themselves. After flashing the firmware you will need to install those packages again.

Verify firmware file and flash the firmware
-------------------------------------------

  - Connect to the device via Ethernet cable (Use wireless only, if the device has no Ethernet connection options)
  - Log into the LEDE's web admin GUI and in the **System -> Backup/Flash Firmware** menu, go to the "Flash new firmware image" section.
  - **Uncheck**/clear the **"Keep settings"** checkbox**!** (more info regarding the :doc:`"Keep settings" checkbox <admingui-sysupgrade-keepsettings>` and it's rare use cases).
  - Ensure that the LEDE firmware file you are about to flash matches your router model and is called **"....sysupgrade.bin"**, as you will **upgrade** an existing LEDE/OpenWrt system towards a newer LEDE firmware version.
  - In the **"Flash new firmware image"** section, click **"Choose file"** to select the image file, then click "Flash image...". This displays a “Flash Firmware - Verify" page, containing a SHA256 checksum of the image file just uploaded to the router.
  - Check that the firmware-checksum displayed on the web GUI matches the SHA256 checksum from the LEDE downloaded page. If it does not match, do NOT continue, as it is a corrupt file and will likely brick your device.  Note: If you are upgrading from OpenWRT 15.05, the 32 character displayed is an MD5 checksum, not SHA256.  Please verify this MD5 checksum on your operating system before proceeding.
  -  If the checksum matches, click "Proceed". This starts the "System - Flashing ..." along with a spinning wheel and "Waiting for changes to be applied..."
  - It can take several minutes, while the router uploads the firmware image and write it into its flash ROM and finally reboots.
  - The new firmware has been installed. Continue with the next section to check the result.

Troubleshooting:
  * if the checksum process failed, do NOT start flashing, as the download could be corrupt. A corrupt firmware file can brick your device! Instead repeat this howto with another download attempt from the download section.
  * if the checksum step fails repeatedly, you can consult the `"Installing and Using LEDE" Forum <https://forum.lede-project.org/c/installation>`_ for help. Be sure to include the exact brand, model, and version of your device.

Check flash result
------------------

  * After your device has finished flashing and rebooting, check if you can access the web admin GUI of LEDE on it's default IP: http://192.168.1.1 (or the IP that you know of)

Troubleshooting:
  * If you have flashed a development/snapshot firmware of LEDE, you first need to manually enable the admin web GUI: :doc:`development installation guide <developmentinstallation>`. Or verify the result by SSH-connecting to your LEDE device IP 192.168.1.1
  * The router may have succeeded, but gotten a different IP address than you expected. Either scan your local network, check your regular router's status page (to find out about the IP address it has assigned to your LEDE device) or use :doc:`failsafe mode </user-guide/failsafe_and_factory_reset>`, to manually reset LEDE's settings (which includes the network settings)
  * If you have checkmarked the "Keep settings" checkbox in the previous section and the system fails to boot after flashing, you need to consult the :doc:`failsafe mode </user-guide/failsafe_and_factory_reset>`, to manually reset all settings.


Install additional packages
---------------------------

  * You may now want to reinstall the custom packages that you had before the sysupgrade, by using ''opkg''.
  * If any package installs a system service, you also need to enable the corresponding service according to your needs.

Restore backed up LEDE configuration
------------------------------------

  * If you have chosen to backup your previous config in the previous step, you can now restore it, using LuCi's **System > Backup/flash firmware** menu.
  * Otherwise you need to start configuring from scratch. In this case, remember to properly **set your country code in the LEDE WiFi configuration** again, to comply with your country's WiFi legal regulation, e.g. see in :doc:`basic WiFi setup <basic_wifi>`.

