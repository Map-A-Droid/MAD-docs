=============
Android TV (ATV)
=============

Map-A-Droid currently has support for both 32-bit and 64-bit architecture. Niantic has previously indicated 32-bit architecture support will be dropped in future releases. Be aware of the ATV's architecture when purchasing.

ATV's can have custom firmware(MADRom) flashed that will enable quick deployment of fully configured devices.
All current Official MADRom releases are located `here <https://github.com/Map-A-Droid/MAD-ATV/releases>`_.

Both 64-bit and 32-bit architecture ATV's follow the same basic steps for MAD configuration.
 * Download the correct MADRom for the device model. Refer to `Download ROM <https://github.com/Map-A-Droid/MAD-ATV/wiki#download-rom>`_ for more information.
   * 32-bit MADRoms are generic while 64-bit MADRoms are device-specific
   
 * Flash the device with the appropriate flashing method. Refer to `Flashing instructions <https://github.com/Map-A-Droid/MAD-ATV/wiki#flashing-instructions>`_ for more information.
 * Configure the device. Refer to the appropriate architecture section below for specific configuration instructions.

32-bit
--------
The official 32-bit MADRom supports either manual or limited interation configurations. Initial MADRom configuration will install Magisk and smali location patching. 
Refer to `ATV Installation <https://github.com/Map-A-Droid/MAD-ATV/blob/master/README_installation.md>`_ for more detailed information.

64-bit
---------
The official 64-bit MADRom supports either manual or automatic configuration. Initial instillation will install Magisk on first boot. Flashing smali mock location module is not required when using an official MADRom. 

The recommended installation configuration path is using the :ref:`Auto-Configuration wizard <sec_auto_conf>`.

Additional Info
================
If you're looking for ways to modify your ATV and enhance your setup (3D printed cases, alternate power supplies etc), please see `PimpMyAtv <https://github.com/madBeavis/PimpMyAtv>`_ for more information.
