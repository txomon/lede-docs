Installing LEDE Development Snapshots
=====================================

**For experienced users only!**

The steps below install LEDE development snapshot firmware on your device.

What is a development snapshot firmware?
----------------------------------------

Development snapshots are also known as simply "snapshots" or the outdated term "trunk builds". Snapshots are versions of LEDE that are "in development". They are rebuilt frequently, often multiple times a day.

I am a standard consumer, do I want a development snapshot firmware?
--------------------------------------------------------------------

**No!** Although they are the latest version, there is no guarantee that any particular snapshot build will be bug-free, or even work at all.\\
Snapshots are not likely to be stable enough to be used on your home router, where you or members of your family rely on the network.\\
As a standard consumer stick to the official release versions of LEDE.

Snapshots do not have LuCi web admin GUI installed by default
-------------------------------------------------------------

On snapshots, LuCi has to be installed manually (if needed).

Manual LuCi installation by package may require more free flash storage than a 4MB-flash-device can handle, `see 4/32 device warning <meta:infobox:432_warning>`_

To manually install LuCi: `LuCI installation <user-guide/luci:Essentials>`_

Installing a LEDE Snapshot
--------------------------

To install (or "flash") a LEDE snapshot firmware image, just follow the standard flashing instructions: `Factory install <quick-start:factory_installation>`_ and `Sysupgrade <quick-start/sysupgrade:luci>`_, with the only difference to use it for a firmware file from the snapshot download section.

Optional Next Steps
-------------------

Once the snapshot is installed on your device
  * `Install LuCI <user-guide:luci:Essentials>`_, if required
  * Consult the `User Guide <user-guide>`_
  * Install other packages with `opkg install ...`
    * You should definitely install the **SQM-QoS package** to minimize lag/latency. Use `opkg install luci-app-sqm`, then read how to configure it in the `SQM Howto <https://lede-project.org/docs/howto/sqm>`_.
    * Other useful packages are snmpd, netperf, and any of your favorites.
  * If you have an unbranded / low-end / low-cost router that came shipped with OpenWrt / LEDE, you can find out the architecture it is using by connecting to it over ssh and opening `/proc/cpuinfo`. A combination of the `system type` and `machine` is what you are looking for.
  * If you will be flashing LEDE snapshot firmware frequently, you can create a script that makes configuration changes in a reliable and repeatable fashion. See, for example, the `config-openwrt.sh <https://github.com/richb-hanover/OpenWrtScripts/blob/master/config-openwrt.sh>`_ script that updates most settings.
