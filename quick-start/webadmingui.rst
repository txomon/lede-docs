Accessing the LEDE web admin GUI
================================

LEDE has a web admin GUI called "LuCi".

  * If your LEDE device has been configured as a router or gateway with default settings, LuCi is listening on your local IP subnet's default gateway address http://192.168.1.1.
  * If your LEDE device has been configured as WiFi access point, network client or switch, LuCi's address depends on the IP address you have manually configured for your LEDE device. You can also try, to use a local network scanner or your regular router's status page to find out the device IP address.

You need to use the "root" password to successfully access LuCi, 'root' is the default admin account of your LEDE device. On a freshly installed LEDE device, there is no password set yet for the 'root' account, you can just enter right away. Please make sure, to set an individual 'root' password as soon as possible.

If you are unable to access your LEDE device, due to messed up IP address/root password configuration, refer to the troubleshooting section of the user guide, to reset the LEDE device's settings.
