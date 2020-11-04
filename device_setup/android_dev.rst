===============
Android Device
===============

You need a device that is rooted with Magisk, Smali patched (optional, but recommended), PogoDroid and Remote GPS Controller (RGC) installed.

#. Install Team Win Recovery Project (TWRP)
#. Install Magisk
#. Install the game
#. Install and configure RemoteGPSController and PogoDroid

Get started
-----------

For a list of confirmed devices that working with MAD, check out `this list <https://github.com/Map-A-Droid/MAD-device-list>`_.

Your device needs to have an unlocked bootloader and must be able to support applications running as root. It is recommended that you install `Lineage OS <https://lineageos.org>`_. They have good instructions for each device. Make sure to install the Play Store as described in the Lineage instructions.

If you feel confident to do so you can use a different OS, however, Lineage is recommended.

Always check the exact version of the device, some versions do not work with some ROMs. For example, Samsung has numerous versions numbers of the S5. Some are able to install Lineage and others are not. Lineage lists the device version numbers that it is compatible with.

Once you have Lineage installed and the Google Apps with the Play Store, move on to root your device with Magisk.

.. note::
  Your Android ROM needs to pass Android's SafetyNet check. Make sure to test it via `this app <https://play.google.com/store/apps/details?id=com.scottyab.safetynet.sample>`_ before you continue. Usually official LineageOS ROMs do pass the check.

Magisk
^^^^^^
.. warning::
  There is currently a bug in the very latest Magisk version that prevents our apps from clicking on the screen (which is needed for several scanning modes). It may work on your device, you have to try it or use Magisk 19.0 or lower to avoid this!

.. warning::
  The hideoption with Magisk version **20.4** is not activated by default. Please activate that function by yourself in the magisk settings first!

#. Install `Magisk <https://www.xda-developers.com/how-to-install-magisk>`_ to root the device via recovery. Download it `here <https://github.com/topjohnwu/Magisk/releases>`_
#. Repackage the MagiskManager App and make sure to delete the folder "/sdcard/MagiskManager" after repackaging. If its not present, you are good to go.

Smali Patcher
^^^^^^^^^^^^^

The Smali Patcher is a little program able to patch Android's internal system files. This will allow you to use the "Mock Location" feature within Android without any apps knowing about it.

#. Follow the instructions to download and install it from the `Smali Patcher forum <https://forum.xda-developers.com/apps/magisk/module-smali-patcher-0-7-t3680053>`_
#. You can ether install it via TWRP or via the Magisk module option in the Magisk Manager.
#. Reboot to TWRP to delete the Davlik and the normal Cache. (WARNING: The TWRP-screen may potentially trigger seizures for people with photosensitive epilepsy.)

Applications
------------

The game
^^^^^^^^

Install the latest supported game version from the Play Store or download it from `apkmirror.com <https://www.apkmirror.com/apk/niantic-inc/pokemon-go/>`_. Make sure to add it in :menuselection:`Magisk Manager --> Magisk Hide`!

Remote GPS Controller
^^^^^^^^^^^^^^^^^^^^^^

`Download Remote GPS Controller (RGC) <https://github.com/Map-A-Droid/MAD/blob/master/APK/RemoteGpsController.apk>`_ first.

RGC must be converted to a system app after it is installed. There are two ways to do this, Link2sd or Systemizer Magisk Module. Link2sd is a bit easier to use but sometimes fails, the Magsisk Module is more reliable but a little bit more complex to use. Choose option #2 (priv-app) when using the Module.

Install `Link2sd <https://play.google.com/store/apps/details?id=com.buak.Link2SD>`_ to systemize RGC. Once installed go into Link2sd, you may be prompted to give it superuser access, if so do accept this. Scroll down and find RGC. Click on it, go to the menu and convert RGC to a system app. It may ask you to reboot if so do so.

.. tip::
  If Link2sd fails to systemize correctly, try `App Systemizer for Magisk <https://forum.xda-developers.com/apps/magisk/module-app-systemizer-t3477512>`_ instead

In Android go to :menuselection:`Settings --> Developer Options --> Select mock location app` and choose "RemoteGPSController".

Open RGC for the first time. A popup will appear to grant superuser permissions to the app. Approve this. If the popup did not appear, you might've missted it. Go to :menuselection:`Magisk Manager --> Superuser --> enable the game`.

Now you can configure RGC.

.. TODO make this a table?

* Socket section

  * **Websocket URI**: ws://ipofyourserver:8080. Default port is 8080, you can change this in MAD's config.ini
  * **Websocket Origin**: pick a short unique name for your device. The name must've been configured in MAD as well
  * **Auth**: optional, configure that via the MADmin Auth settings

* Rooted devices section

  * **Reset GMS data**: Off. Keep it off unless you face any GPS issues like rubberbanding
  * **Override OOM**: On. This will help to keep RGC running

* Location Section

  * **Reset AGPS data continuously**: Off. Turn this on when mock location is not used
  * **Reset AGPS once**: Off. Turn this on when mock location is not used
  * **Use Android Mock Location**: On

* General Section

  * **Start on Boot**: On
  * **Start RGC Delay**: 30. Play around with this setting. It's best practice to start RGC after PogoDroid to ensure that PogoDroid is injected before RGC connects starts and connects to MAD
  * **Start services on app start**: On

PogoDroid
^^^^^^^^^

#. Install `PogoDroid <https://www.maddev.eu/apk/PogoDroid.apk>`_ on your device
#. To login to PogoDroid you need to purchase a license from the `MADDev shop <https://maddev.eu/>`_ and follow the instructions.
#. Once logged into the `backend <http://auth.maddev.eu/>`_, click "Password management" on the top
#. On the password page it should tell you your maximum allowed device count. Create a new device password and copy that
#. Go back to PogoDroid. Use your email address and that new device password you've just created in the previous step.

Now you can configure PogoDroid.

.. TODO make this a table?

* External Communication Section

  * **Disable external comm**: Off
  * **Send selected set of serialized data (json)**: On. If your workers get stuck in the ocean even though PogoDroid says it is injected, disable and re-enable this setting
  * **Post Destination**: http://ipofyourserver:8000. Default port is 8000, you can change that in the config.ini)
  * **Post Origin**: This value needs to match the value you entered in RGC
  * **Disable last sent notifications**: Your decision, but some devices pull up the navigation bar while showing the notification which causes issues with questmode
  * **Auth**: optional, configure that via the MADmin Auth settings

* App Section

  * **Repackage**: Repackage Pogodroid to hide itself. Currently broken, dont use it
  * **Export Settings**: Export the Pogodroid settings as a file. Useful to setup other devices with the same settings
  * **Injection Delay**: Play around with that setting
  * **Lower SELinux to permissive**: On. Turn it off when the injection is not successful
  * **Full daemon mode**: On
  * **Start Pogodoid with a delay (seconds)**: Play around with that setting. Best practice is to keep that value lower than the delay from RGC
  * **Enable OOM override**: On
  * **Test feature: Mock location patching**: Off. Try this if you cant smali patch

.. _sec_device_final_steps:
Final Steps
-----------

#. Go into Android Settings, Security, Lock Screen Swipe, change to None. You don't want a lock screen. Locking and unlocking your device should bring you to the desktop
#. Go into Android Settings, Developer Options, Stay Awake, make sure this setting is enabled. This will prevent the screen from locking even if pokemon go isn't running
#. If you want to scan quests with that device make sure to hide the navigation bar for PoGo: :code:`adb shell settings put global policy_control immersive.full=com.nianticlabs.pokemongo`
#. Disable vibration for Pokemon GO if you don't want your whole house shaking.

.. code-block:: bash

  adb shell "cmd appops set com.nianticlabs.pokemongo VIBRATE ignore"

#. Before we finish, go inside of Magisk and run the Safetynet Check one last time. You need to see all green before proceeding
