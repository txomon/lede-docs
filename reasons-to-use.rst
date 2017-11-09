Reasons to Use LEDE
===================

People install LEDE because they find it to be superior to the stock firmware of their router or embedded device. This page showcases many aspects of LEDE.


Performance & Stability
-----------------------

LEDE is designed by network professionals and others who care about the performance of their network. LEDE incorporates many algorithms from recent research that perform far better than vendor-supplied firmware.
  * LEDE is stable, and operates reliably for long periods of time.
  * LEDE reduces latency/lag and increased network throughput via bufferbloat control algorithms.
  * Wi-Fi improvements support higher data rates and airtime fairness between stations.
  * Older devices are still supported by LEDE improvements (as long as RAM/Flash of your device can accommodate new releases) long after the manufacturer stops making updates.


Security
--------

LEDE is an open source software. Many developers from all over the world review the code before it's released.
  * No hidden backdoors left by hardware vendors.
  * LEDE is resistant to common vulnerabilities thanks to its Linux OS which is unaffected by many common attacks.
  * LEDE is actively updated so any vulnerabilities are closed shortly after they are discovered.
  * Default LEDE configuration is very conservative allowing full internet connectivity without exposing your router or connected devices to attacks.
  * Many of the older devices are supported by LEDE and can enjoy security LEDE brings, long after vendors stop releasing firmware updates.
  * LEDE prolongs the life of your router. While many vendors only provide updates for your router/device until the newer model is released, LEDE supports all `compatible models <supported_devices>`_ for as long as their RAM/Flash can accommodate new releases.


Extensibility
-------------

While vendor firmware for a router ships with a fixed set of capabilities, LEDE provides more than `3000 packages <packages>`_ ready to be installed. Some of the more popular packages allow you to:
  * Run `ad blocking <user-guide/ad-blocking>`_ on your router so you can enjoy clean uncluttered web experience from any connected device.
  * Reduce latency/lag (bufferbloat) even during heavy traffic with `Smart Queue Management <docs/user-guide/sqm>`_
  * Secure access to your home network when away via `OpenVPN Server <user-guide:openvpn.server>`_.
  * Secure your internet access and prevent your ISP from snooping on your internet activity (requires third party service) `OpenVPN Client <user-guide/openvpn/client>`_.
  * Prevent your ISP from snooping on your DNS requests via `DNSCrypt Proxy <user-guide:dnscrypt-proxy>`_.
  * Force connected devices with hard-coded DNS servers to use your router's DNS with `DNS Request Hijacking <user-guide/DNS-request-hijacking>`_.
  * Create a `Guest Network for Guest WiFi <user-guide:guestwifi_configuration>`_ allowing access to internet, but not your local devices.
  * Control access using the `time limits and parental controls <user-guide:parental-controls>`_.
  * `Add a webcam <user-guide/webcam>`_ for live surveillance or timelapse video creation of landscapes or 3D printers.
  * `Connect to your weather station <user-guide/weatherstation>`_, record `weather statistics <user-guide/weather:statistics>`_ and make them accessible via a `webserver <user-guide/webserver>`_, garnished with a `live webcam image <user-guide:webcam>`_.
  * `Interact with 1-wire devices <user-guide/1wire>`_ (sensors, actors, ...).
  * Make your router a central for `home automation <user-guide/home automation>`_.
  * Access a wider range of `Dynamic DNS (ddns) <user-guide/ddns:client>`_ providers than vendor firmware via `DDNS scripts <packages/pkgdata/ddns-scripts>`_.


Community Support
-----------------

The vibrant community of developers, volunteers, and other long-time LEDE users are always available to help solve an issue.

  * `LEDE forum <https://forum.lede-project.org>`_ - member-to-member conversations about LEDE
  * `LEDE Developer <http://lists.infradead.org/mailman/listinfo/lede-dev>`_ and `LEDE Admin <http://lists.infradead.org/mailman/listinfo/lede-adm>`_ mailing lists
  * `#lede-dev and #lede-adm <https://webchat.freenode.net/?channels=lede-dev%2Clede-adm>`_ on Freenode IRC
  * Refer to the :doc:`contact page <contact>` for a complete list to contact the project.


Research Platform
-----------------

Many teams who are doing cutting-edge research into networking topics use LEDE as a stable platform for their work. As their work moves from the experimental realm into practical, production-quality code, it is available in LEDE builds first. Some teams using LEDE include:
  * Continuing development of the `fq_codel and cake algorithms <http://bufferbloat.net>`_ that decrease bufferbloat.
  * The `Make Wi-Fi Fast <https://www.bufferbloat.net/projects/make-wifi-fast/wiki/>`_ team has been working to decrease queueing and latency in the wi-fi stack, and is testing out their airtime fairness code using LEDE.
  * `Homenet <http://homewrt.org>`_ provides implementation of zeroconf IPv6 (and IPv4) routing, prefix assignment and service discovery for a home network consisting of multiple routers connected to multiple service providers. There's a hnet-full package for LEDE.



Configuration
-------------

Because LEDE is a true Linux-based system, you have full control over all functions of your router/device.
  * LEDE provides both command-line interface (via SSH) and a web-based user interface for configuration.
  * Configuration information is stored in plain-text files to ease the editing and/or copying.
  * LEDE Image Builder allows you to create your own firmware images for your device with any customizations (pre-defined password, WiFi, etc).
  * The Web GUI allows you to select `themes <user-guide/luci:themes>`_ that suit your needs/tastes In addition, `Localization of Web UI <packages/pkgdata/luci-i18n-base-lang>`_ is available via packages in over 20 languages.
  * Configure the external LEDs and buttons/switches to suit your needs.

Zero Cost
---------
LEDE is provided for free through its GPL license, and thanks to the efforts of many volunteer contributors (both individuals and companies). There are no subscription or licensing fees.
