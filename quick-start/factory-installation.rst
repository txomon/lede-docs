Factory install: First-time installation of LEDE on a device
============================================================

Your device must still have the vendor firmware to be eligible for this so-called "factory installation" procedure.
  * If your device already has an older LEDE or OpenWrt firmware on it, refer to the `sysupgrade <quick-start/sysupgrade>`_ howto instead .
  * If you have any questions about this description, ask for help on the `Installing and Using LEDE forum section <https://forum.lede-project.org/c/installation>`_ before beginning.

Device selection
----------------

  * Devices with >=8 MBytes Flash memory and >=64 MBytes RAM allow a full-featured LEDE installation with GUI.
  * Devices with 4 MByte or less Flash memory can install LEDE as well, but with a limited feature set. They cannot use optional packages and in some cases may also not have a web GUI, due to limited flash space and may therefore have to stick to command line administration only. The creation of individual custom packages may help to avoid some of these limitations on such 'small' devices, but such a custom-package-creation is not part of this howto.
  * If you want to purchase a new router for LEDE, stick to devices with >=8 MBytes Flash memory and >=64 MBytes RAM.

Locate and download the LEDE firmware
-------------------------------------

  - On the `Table of Hardware: Firmware downloads <toh_fwdownload>`_ page, locate your specific device. The table of hardware only references stable release versions of LEDE. If you are a newbee, only use these stable release version for first-time device installations; do not initially use a (clearly marked) develop/snapshot version downloaded from other subfolders. This ensures that you get the easiest possible first-time LEDE installation experience.
  - When you have located your device in this list, click on the "View/edit data" link of the device record. This will open a new page with several details for your specific device. We recommend to bookmark that page, as it has lots of helpful information about your router.
  - On this device-specific **Techdata** page, at the bottom locate the line called **"Firmware LEDE Install URL"** that links to a downloadable file called **"...factory.bin"** file.
  - Download this file.

Troubleshooting:
  * Some devices lack a factory image and require a special (and usually a bit more complex) installation procedure that is device-specific. This tutorial won't apply for such devices. If you have such a device, locate the corresponding device page in the older OpenWrt wiki and follow the custom installation description (Eventually older OpenWrt info will be migrated to the LEDE tech data pages).
  * If you can't find your device in the Table of Hardware, or if there is no "...factory.bin" file, you can consult the `"Installing and Using LEDE" Forum <https://forum.lede-project.org/c/installation>`_ for help. You can also try `alternative ways to locate LEDE firmware images <quick-start:alternate-directory-search>`_
  * If you have accidentally browsed the generic LEDE download folders to locate your device, you might see some more download files matching your device. Ignore those other files for your device: you only want the "...factory.bin" file.

Verify the downloaded firmware file
-----------------------------------

You will now use a checksum tool, to calculate a checksum from your downloaded file and then compare this calculated checksum  with the file-specific checksum listed on the firmware download site.
This ensures that you have a 100% correct download and that you will not brick your device by applying a faulty download.

  - Check your downloaded "...factory.bin" file according to `checksum verification of downloaded LEDE firmware files <quick-start/verify_firmware_checksum>`_.
  - Only continue with flashing, if the firmware checksum of your download matches the checksum stated on the download site!

Troubleshooting:
  * if the checksum process has reported a checksum mismatch, do NOT start flashing, as the download could be corrupt. A corrupt firmware file can brick your device! Instead retry with another download attempt and retry the checksum step.
  * if the checksum step fails repeatedly, you can consult the `"Installing and Using LEDE" Forum <https://forum.lede-project.org/c/installation>`_ for help. Be sure to include the exact brand, model, and version of your device.

Flash the firmware
------------------

  - Connect to the device via Ethernet cable (Only fallback to wireless, if the device has no Ethernet connection options)
  - Ensure that the LEDE firmware file that you are about to flash, matches your router model and is called **"....factory.bin"**, as you will use it to modify a vendor's **factory** firmware towards LEDE.
  -  Log into the device's admin web interface and locate the device-specific firmware installation function. Follow the device-specific instructions of your manufacturer's user guide for installing firmware and use this to install the  "...factory.bin" firmware file of LEDE.
  - Wait while the device writes the firmware image to its flash memory. This can take several minutes (the Device Page may state an expected time for this process). At the end, the device will reboot automatically.
  - The new firmware has been installed. Continue with the next section to check the result.

Check flash result
------------------

  - After your device has finished flashing and rebooting, check if you can access the LEDE web admin GUI of LEDE on LEDE's default IP address: http://192.168.1.1
  - Login to the LEDE web GUI as "root" admin user with the password field empty
  - Go to the System->Administration page and define a new password in both fields, then click Save and Apply (at the bottom of the page).
  - This has verified that you can successfully use the LAN ports of your LEDE device. You now have a working LEDE device in its initial default configuration.

Troubleshooting:
  * For this check only use an Ethernet cable, as WiFi is by default only enabled for devices that do not have Ethernet ports
  * If you have flashed a development/snapshot firmware of LEDE, you first need to manually enable the admin web GUI: `development installation guide <quick-start:developmentinstallation>`_. Or verify the result on snapshot builds by SSH-connecting to your LEDE device IP 192.168.1.1
  * You can consult the troubleshooting section of the `User Guide <user-guide/start>`_, if you think that resetting LEDE's settings might help.
  * You can consult the `Installing and Using LEDE forum section <https://forum.lede-project.org/c/installation>`_, if something went wrong. Please provide specific details of your device and what you did so far and what you have attempted to fix it.

Next steps
----------

  * For a first quick Internet access test: If you have an existing router, connect the WAN port of your LEDE device to a LAN port of that router and confirm internet connectivity of your LEDE device with the following steps:
     * In the LEDE admin web GUI, go to Network -> Diagnostics and Click on "ping" button
     * or, if using LEDE SSH command line, you can use the command ''ping lede-project.org''
     * This should return "0% packet loss" if everything is allright with your Internet connection.
  * Decide, whether you want to use LEDE `as switch,  router or gateway <user-guide/switch_router_gateway_and_nat>`_
  * **When using your LEDE device as a WiFi access point, remember to initially set your country code in the LEDE WiFi configuration, to properly comply with your country's WiFi legal regulation!**, e.g. see here for a first `basic WiFi setup <quick-start/basic_wifi>`_.
  * Consult the `User Guide <user-guide>`_ for more advanced configuration.
  * Install custom software packages that you might be interested in.

Troubleshooting your first steps with the new LEDE device
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

  * Do not worry, if the 5 GHz WiFi does not seem to start immediately after having enabled it. It might be busy for 1-10 min scanning for weather radar, see `basic WiFi setup <quick-start:basic_wifi>`_ for more background info.
  * Note that you can always run ''logread'' on the SSH command line, to gain more insight into what the device is currently doing or to diagnose any kind of problems.
  * If needed, you can also take a look at `Troubleshooting Internet Connectivity <quick-start:ts-internetconnectivity>`_].
