Enabling a Wi-Fi access point on your LEDE device
=================================================

Devices that have ethernet ports have Wi-Fi turned off by default.
This is a basic description, how to enable a first WiFi network and most important, how to properly configure your country code such that your WiFi network complies with the legal regulation of your country.

On web admin GUI
----------------

  - Open the admin GUI on http://192.168.1.1
  - Login with your "root" password
  - Go to the menu Network → Wireless. This page list a separate WiFi configuration section for each of your pysical radios, (many devices you will have a first radio for 2.4 GHz and a second one for 5 GHz).
  - For each of your radios, you can create a WiFi network by clicking ''Add'':

    - On the first WiFi network that you configure, go to the **Device Configuration** and open the tab **Advanced Settings**: in the ''Country Code'' field, select the correct county code, where your LEDE device is installed. This is important to ensure your LEDE device meets legal regulations in your country. (all other configured radios will use the same device settings)
    - For each WiFi network, in the "Interface Configuration" section, configure your WiFi settings, at least customizing the following settings:

      * In the tab **General Setup**, define a custom ''ESSID'' (the name of your WiFi network)
      * In the tab **Wireless Security**, activate some ''Encryption'' (e,g, "WPA2-PSK")
      * In the tab **Wireless Security**, activate a ''Cipher'' (e.g. "Force CCMP AES")
      * In the tab **Wireless Security**, in ''Key'', define a personal secret phrase, which clients need to use, to successfully connect to your WiFi network.
      * If needed, configure further settings according to your needs. often the default settings like **auto** are sufficient for general usage.

  - Click ''Save & Apply'' when done.

Troubleshooting:
  * If you have configured 5GHz WiFi and have just enabled it, but the 5 GHz WiFi does not seem to start up, consider the following: If your device supports WiFi channels > 100, your LEDE device first must scan for weather radar on these channels, before you can actually use such channels for WiFi. This may take 1-10 minutes onetime after first reboot depending on your WiFi situation and depending on the number of device-supported channels > 100. You may also experience 1 minute delay on each automatic channel change, as the same scan delay is required for regulation compliance.

On SSH command line
-------------------

This is not a complete howto, to create a WiFi network on the command line.\\
It just shows you the important step, to initially set your country code for proper WiFi on the command line, to meet legal regulations of your country:

  * Connect with SSH to your LEDE device.
  * Execute ''uci show wireless'' to see all the wireless configuration and how many Wi-Fi chips (called “radio” in the config) there are on the device
  * Find out your country in a list of ISO/IEC 3166 alpha2 country codes. There is a list on the wikipedia article about ISO 3166-1 alpha-2
  * Execute ''uci set wireless.radio0.country='XX' '' to set the country code XX for radio0 device, and adjust this command to set the same country code for all wireless radios in the device.

