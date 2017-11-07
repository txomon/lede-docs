====== Verifying LEDE firmware binary ======
This step is to verify a downloaded firmware binary against a reference checksum to avoid download errors.

Obtaining the reference checksum from the download page is currently a little inconvenient, as the reference checksums of the firmware binaries are currently not listed on the LEDE device tech data pages.

To get the reference checksum, recall the URL path of firmware binary you just downloaded, e.g. if your firmware download-URL was\\ https://downloads.lede-project.org/releases/version/targets/chipset/modell/lede-something-something-something-something-something.bin\\
then open the web page https://downloads.lede-project.org/releases/version/targets/chipset/modell/

There you will find a list of firmware images, one of it being the file you just downloaded. Now note the additional checksum string on the right side of the download link (in the table column "sha256sum").

We will now calculate a checksum of the downloaded file and compare it with that string. If that check fails, the firmware file was not properly downloaded and if you proceed flashing such a file, you will probably brick the device permanently or requiring annoying procedures to recover.

  * On checksum mismatches, download the firmware file again and compare it again.
  * if the checksum is still wrong in repeated attempts, ask the LEDE forums for help.

===== Calculating checksum of a LEDE firmware download on Windows =====

  * Newer Windows has a built-in tool to calculate sha256sums called 'certutil', but it has no graphical user interface so we will have to use the command line to interact with it.
  * Older Windows version need to download a sha256 tool, for example [[https://raylin.wordpress.com/downloads/md5-sha-1-checksum-utility/|MD5 & SHA Checksum Utility]] (the free version).

To use the built-in "certutil:
  - Click the Windows icon, type "cmd" and hit enter.
  - Execute (assuming you downloaded the file to your Downloads folder): <code>certutil -hashfile "%USERPROFILE%/Downloads/LEDE-file-name-here" sha256</code>
  - This will print a checksum like this (file name followed by string with letters and numbers), <code>SHA256-Hash of file C:\Users\USERNAME\Downloads\lede-17.01.1-...-factory.bin:
79 f9 4e fa d3 2c 14 8f f1 95 3f 09 6d 98 c7 41 c0 ff 8f 7e b4 68 8c 9d 5b f9 fb 01 c0 90 fb ab</code> 
  - Remove spaces from this checksum output (e.g. using replace function in notepad):<code>79f94efad32c148ff1953f096d98c741c0ff8f7eb4688c9d5bf9fb01c090fbab</code> 
  -  Check that the checksum string without blanks matches the one you can find in the **sha256sums** field on the download page.

===== Calculating checksum of a LEDE firmware download on Mac =====

Mac has an integrated tool to check sha256sums, but it has no graphical user interface so we will have to use the Terminal to interact with it.
  - Click the Finder icon in the Dock. 
  - Click Applications in the Favorites list.
  - Find the Utilities folder and click to open it.
  - Locate Terminal and double-click the icon to open the program.
  - Open a terminal window, and execute (assuming you downloaded the file on the desktop): <code>shasum -a 256 ./Desktop/file-name-here</code>
  - it will print something like this (string with letters and numbers followed by file name),<code>1a7c8bba93584fc44045629888e6b147851917cd0c83fcc91a7e6dbe90bdce76 
lede-17.01.0-...-sysupgrade.bin</code>
  - Check that the checksum string matches the one you can find in the **sha256sums** field on the download page.

===== Calculating checksum of a LEDE firmware download on Linux =====

Linux has an integrated tool that is accessible from command line, similar to Mac. 
  * Some file managers (dolphin and other more powerful ones used in KDE user interface) offer this functionality in the file property window (right-click on the file, select Properties, click on "Checksums" tab, that tab appears only for binary files, like firmware images). It will offer buttons to calculate the SHA256sum and a field where you can paste the SHA256 string from sha256sums file to verify that it is correct.
  * If your file manager does not offer any of this, you can always use the terminal window and type in the following command (again assuming you downloaded the file on the desktop)

Command line verification:
  - On the terminal window, execute <code>sha256sum ./Desktop/file-name-here</code>
  - This will print something like this: <code>1a7c8bba93584fc44045629888e6b147851917cd0c83fcc91a7e6dbe90bdce76
lede-17.01.0-...-sysupgrade.bin</code>
  - Check that the checksum string matches as the one you can find in the **sha256sums** field on the download page.
