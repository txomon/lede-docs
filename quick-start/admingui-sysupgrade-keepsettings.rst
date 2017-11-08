Web GUI Sysupgrade: The "Keep settings" checkbox
================================================

The "Keep settings" checkbox is a more advanced feature.

If you do not precisely understand the button's use cases, **uncheck "Keep Settings"** every time you flash a new LEDE sysupgrade to your device, to **not** preserve settings.

  * Only check the "Keep settings" checkbox on minor LEDE->LEDE bug fix upgrades that are known to not change the config structure
  * Only use it for the same firmware channel (release->release, snapshot->snapshot)
  * Checking it will preserve several specific config files on the upgrade, but not the whole overlay partition.
  * If you flash your device regularly, preferably consider unchecking "Keep Settings" every time you flash the router and instead create a custom installation script for your customization. Example: `config-openwrt.sh <https://github.com/richb-hanover/OpenWrtScripts/blob/master/config-openwrt.sh>`_ script.
  * "Keep settings" can also be used to preserve own configurations files. To do, go to **System > Backup/Flash Firmware** and open the **Configuration** tab, add your config filesthere and click "Submit". This will allow you to add your custom configuration files to the ''/etc/sysupgrade.conf'' file that is read by sysupgrade when it is backing up files. Click "Submit" when done editing.\\ To view all files that would be kept when "keep settings" is checked, click the "**Open list...**" button.
