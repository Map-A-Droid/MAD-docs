# Phone Setup

You need a phone that is rooted with Magisk, Smali patched (optional, but recommended), PogoDroid (only for MITM mode) and RGC installed.

- Install TWRP
- Install Magisk
- Install PoGo
- Install and configure RGC and PogoDroid

## Phone Install

If you are not sure which phone is viable, check out [this list](https://github.com/Map-A-Droid/MAD-device-list). Some phones need to be a certain version number to work, see below.

Your phone needs to have an unlocked bootloader and be able to support applications running as root. Its recommended that you install [Lineage OS](https://lineageos.org/).  They have good installation instructions for each device.  Make sure to install the Playstore as described in the Lineage instructions. If you are an expert you can use a different OS, if not use Lineage.
>Always check the exact version of the phone, some version does not work with some ROMs. For ex. Samsung has numerous versions numbers of the S5. Some are able to install Lineage and others are not. Lineage lists the phone version numbers that it is compatible with.

>Samsung S5 G900V and G900A are confirmed NOT to work. G900T DOES work.
Moto G4 works, but the Amazon edition of the Moto G4 (Moto G4 Play) does NOT work.

Once you have Lineage installed and the Google Apps with the Playstore, move on to Magisk.

## Magisk

1. Install [Magisk](https://www.xda-developers.com/how-to-install-magisk/) to root the phone via recovery. Download it [here](https://github.com/topjohnwu/Magisk/releases)
     >There is currently a bug in the very latest Magisk version that prevents RGC from clicking on the screen (which is needed for questscanning), use Magisk 19.0 or lower to avoid this.

2. Repackage the MagiskManager App and make sure to delete the folder `/sdcard/MagiskManager` after repackaging. If its not present, you are good to go.

## Smali Patcher

The Smali Patcher is a little program written in Java to patch a android file called `services.jar`. That will allow you to use the "mock location" feature from Android.

1. Follow the instructions here to download and install it from the [Smali Patcher Forum](https://forum.xda-developers.com/apps/magisk/module-smali-patcher-0-7-t3680053)
2. You can ether install it via TWRP or via the magisk module option in the magisk manager.
3. Reboot to TWRP to delete the Davlik and the normal Cache.

## Applications - PoGo, RGC & PogoDroid

### Pokémon Go

Install the latest supported PoGo app from the Play Store or [apkmirror.com](https://www.apkmirror.com/apk/niantic-inc/pokemon-go/) and add PoGo to Magisk Hide via the magisk manager.

>It's necessary to pass the Safetynet check to run the game on rooted phones. Check the Safetynet status in the MagiskManager App.

### RGC

RGC - Install [RGC (Remote GPS Controller)](https://github.com/Map-A-Droid/MAD/blob/master/APK/RemoteGpsController.apk)

- RGC must be converted to a system app after it is installed.  There are two ways to do this, link2sd and Systemizer Magisk Module.  Start with Link2sd and then go to Systemizer if it doesnt work.

- Install [Link2sd](https://play.google.com/store/apps/details?id=com.buak.Link2SD) to systemize RGC. Once installed go into Link2sd, you may be prompted to give it super user, if so do it.  Scroll down and find RGC.  Click on it, go to the menu and convert RGC to a system app.  It may ask you to reboot, if so do so.

- If Link2sd didn't work try the Systemizer Magisk Module. You can find the download and instructions here [Systemizer Magisk Module](https://forum.xda-developers.com/apps/magisk/module-app-systemizer-t3477512)

- In Android go into `Settings`, `Developer Options`.  Click on `Select mock location App`, select RGC.

- Open RGC, grant it super user rights if asked.  Select allow for anything it asks access for.

Configure RGC:

#### Socket section

- **Websocket URI** = `ws://ipofyourserver:8080` (Default port is 8080, you can change that in the config.ini)
- **Websocket Origin** = pick a short name for your phone, this will need to match what you put in PogoDroid.  This Origin needs to be unique per running python instance.
- **Auth** = optional, configure that via the mappings.

#### Rooted devices section

- **Reset GMS data** = Start with it Off and turn it to on if you need to troubleshoot Rubberbanding issues.
- **Override OOM** = On. This will help to keep RGC running.

#### Location Section

- **Reset AGPS data continuously** = Off (turn this on when mock location is not used)
- **Reset AGPS once** = Off (turn this on when mock location is not used)
- **Use Android Mock Location** = On

#### General Section

- Start on Boot = On
- Start RGC Delay = 30 (Play around with this setting. It's best practice to start RGC after PogoDroid to ensure that PogoDroid can inject properly.)
- Start services on appstart = On

### PogoDroid

1. Install [PogoDroid](https://www.maddev.de/apk/PogoDroid.apk) (only necessary for MITM mode) on the phone.

2. To login to PogoDroid you need to be a [Patreon supporter](https://www.patreon.com/user?u=14159560).  Become a supporter and link your account to Discord.  

3. Click "Get Refresh Token", then when you get to the next page it will tell you to copy a password and API Token.  Copy both, put them in a notepad (if you dont have a notepad app, nows the time to get one).

4. On next screen login with the password they just gave you.  

5. Once logged in, click "Password management" on the top.

6. On the password page it should tell you your Device Count allowed. Create a new device password and copy that.

7. Go back to PogoDroid.  Use your email address and that new "Device Password" you setup in the previous step.

8. Now it's time to configure PogoDroid.

#### External Communication Section

- **Disable external comm** = Off
- **Post Destination** = `http://ipofyourserver:8000` (Default port is 8000, you can change that in the config.ini)
- **Post Origin** = Make this match what you put in RGC.  
- **Disable last sent notifications** = Your decision, but some devices pull up the navigation bar while showing the notifcation wich is is disturbing the questmode.
- **Auth** = optional, configure that via the mappings.

#### App Section

- **Repackage** - Repackage Pogodroid to hide itself. Currently broken, dont use it.
- **Export Settings** - Export the Pogodroid settings as a file. Useful to setup other devices with the same settings.
- **Injection Delay** - Play around with that setting.
- **Lower SELinux to permissive** = On, turn it off when the injection is not successful.
- **Full daemon mode** = On
- **Start Pogodoid with a delay (seconds)** - Play around with that setting. Best practice is to keep that value lower than the delay from RGC.
- **Enable OOM override** = On
- **Test feature: Mock location patching** = Off. Try this if you cant smali patch.

## Final Steps

- Go into Android Settings, Security, Lock Screen Swipe, change to None.  You dont want a lock screen. Locking and unlocking your phone should bring you right to the desktop.
- If you want to scan quests with that device make sure to hide the navigationbar for PoGo: `adb shell settings put global policy_control immersive.full=com.nianticlabs.pokemongo`.
- Before we finish, go inside of Magisk and run the Safetynet Check one last time. You need to see all green before proceeding.
