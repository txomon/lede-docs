Troubleshooting Internet Connectivity
=====================================

Use these steps if you can connect to your LEDE router's Web GUI, but cannot connect to the broader Internet (say, www.google.com):

  - Verify that the WAN connection of your router (usually Ethernet) is connected to your cable/DSL modem, or other device that's connected "to the internet".
  - Check to see if your LAN and WAN ports are in the same address range. To do this:
    * Go to **Network -> Interfaces**
    * Find the IPv4 address assigned to the **LAN** interface
    * Find the IPv4 address assigned to the **WAN** interface
    * If these two addresses are in the same range, e.g., if they start with the same three sets of numbers, then they are in the same address range. You need to change the address of the LAN interface (see next step).
    * If the address ranges do not conflict, then ask on the [[https://forum.lede-project.org|LEDE Forum]] for more help.
  - Change the LAN interface address, if necessary. To do this:
    * From the **Network -> Interfaces** page, click the **Edit** button next to the LAN interface.
    * The "IPv4 Address" field will show the LAN address found above.
    * Enter a new address, that differs from the WAN address. For example, the LAN address after a fresh LEDE installation will be ''192.168.1.1''. A good alternate address would be ''192.168.2.1''.
    * Change the field to the new address, then click **Save and Apply** at the bottom of the page.
    * Write the new address on the sticker that you placed on the bottom of your router. (This will save you or your techie friend a ton of time next time you need to work on the router.)
  - After changing the address, you will need to enter the //new address// in your web browser. You should get the LEDE login page again.
  - If you can now access the internet (e.g., www.google.com), you're all set. Continue with the [[:docs:guide-quick-start:start|Quick Start Guide.]]
  - If you still cannot access the internet, then ask on the [[https://forum.lede-project.org|LEDE Forum]] for more help.
