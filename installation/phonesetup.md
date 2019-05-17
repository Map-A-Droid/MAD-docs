# Phone Setup

## Contents
- Lineage Install
- Magisk and Smali Patcher
- Pogo
- RGC
- Link2sd / Systemizer Magisk Module
- PogoDroid
- Final Steps
- Rubberbanding troubleshooting (GPS being jumpy)

## Summary of what your about to do
You need a phone with root access, running Lineage OS, with Magisk, Smali, PogoDroid and RGC installed.  
Summary of the phone requirements.
- You need a phone on the MAD device list.
- Your phone also has to be compatible with Lineage OS, which means it needs a bootloader that can be unlocked.
- A phone model frequently has different versions, some compatible, some not.  ex. The Samsung Galaxy S5 G900V and G900A are confirmed NOT to work.  G900T DOES work. 
- While installing Lineage you need to install Google Apps.
- Next you install Magisk and Smali to give applications on your phone super user rights.
- Then install Pogo.
- Finally install and configure RGC and PogoDroid

## Phone and Lineage Install

1. Phone - Aquire one of the phones on this list.  (https://github.com/Map-A-Droid/MAD-device-list).  Some phones need to be a certain version number to work, see below.

2. Lineage OS - Your phone needs to have an unlocked bootloader and be able to support applications running as root. Its recommended that you install [Lineage OS](https://lineageos.org/).  They have good installation instructions for each device.  Make sure to install the Playstore as described in the Lineage instructions.  If you are an expert you can use a different OS, if not use Lineage.

     * Note, you not only need a phone on the MAD Device List, but you also need a version of that phone that can have Lineage installed.  For ex. Samsung has numerous versions numbers of the S5.  Some can have Lineage installed and others cant.  Lineage lists the phone version numbers that it is compatible with.
     * Samsung S5 G900V and G900A are confirmed NOT to work.  G900T DOES work.
     * Moto G4 works, but the Amazon edition of the Moto G4 that pushes ads does NOT work.

4. Once you have Lineage installed and the Google Apps with the Playstore, move on to Magisk.

## Magisk
1. Magisk - Install [Magisk](https://www.xda-developers.com/how-to-install-magisk/) to root the phone via recovery. 
     * You need version 18.1 of Magisk, nothing else works.
     * You need version 7.1.1 of Magisk Manager or lower.
2. Download it here https://github.com/topjohnwu/Magisk/releases
3. Repackage the MagiskManager App and add to Magisk Hide. Make sure to delete the folder `/sdcard/MagiskManager` after repackaging.

## Smali Patcher version 4.9
I used this to get a Galaxy S5 and Moto G4 to work, I am unsure if its needed on all phones.
1. Follow the instructions here to download and install, here's the [Smali Patcher Forum](https://forum.xda-developers.com/apps/magisk/module-smali-patcher-0-7-t3680053)
2. Download link if you need it [Smali 4.9 download](https://forum.xda-developers.com/apps/magisk/module-smali-patcher-0-7-t3680053)
3. Once you are finished installing and reboot the phone, go into Magisk, Menu, Modules.  You should see Smali Patcher listed.  


## Applications - Pogo, RGC & PogoDroid
### Pogo
1. Pogo - Install the PoGo app from the Play Store.

     1.1. Add Pogo to Magisk Hide

     1.2. Inside of Magisk run the Safetynet Check.  You need to see all green.
>It's necessary to pass the Safetynet check to run the game on rooted phones. Check the Safetynet status in the MagiskManager App.

### RGC

2. RGC - Install [RGC (Remote GPS Controller)](https://github.com/Map-A-Droid/MAD/blob/master/APK/RemoteGpsController.apk)
 
     2.1. RGC must be converted to a system app after it is installed.  There are two ways to do this, link2sd and Systemizer Magisk Module.  Start with Link2sd and then go to Systemizer if it doesnt work.

     2.2. Install [link2sd](https://play.google.com/store/apps/details?id=com.buak.Link2SD).  Once installed go into Link2sd, you may be prompted to give it super user, if so do it.  Scroll down and find RGC.  Click on it, go to the menu and convert RGC to a system app.  It may ask you to reboot, if so do so.

     * If Link2sd didn't work try the Systemizer Magisk Module. You can find the download and instructions here [Systemizer Magisk Module](https://forum.xda-developers.com/apps/magisk/module-app-systemizer-t3477512)

     2.3. In Lineage go into `Settings`, `Developer Options`.  Click on `Select mock location App`, select RGC.

     2.4. Open RGC, grant it super user rights if asked.  Select allow for anything it asks access for.
Here are the configuration options for RGC

**Socket section**
* -Socket = `ws://ipofyourserver:8080`
* -Websocket origin = pick a short name for your phone, this will need to match what you put in PogoDroid.  This Origin needs to be unique per running python instance.
* -Auth = off

**Rooted devices section**
* -Reset GMS data = Off (Galaxy S5 and Moto G4 worked well with this on, but there are mixed results. Start with it Off and turn it to on if you need to troubleshoot Rubberbanding issues)
* -Override OOM = Off

**Location Section**
* -Reset AGPS data continuously = Off
* -Reset AGPS once = Off
* -Use Android Mock Location = On

**General Section**
* -Start on Boot = On
* -Start RGC Delay = 0
* -Start services on appstart = On
* -Start mediaprojection on appstart = Off

### PogoDroid

1. Install [PogoDroid](https://www.maddev.de/apk/PogoDroid.apk) (only necessary for MITM mode) on the phone.
 
2. To login to PogoDroid you need to be a [Patreon supporter](https://www.patreon.com/user?u=14159560).  Become a supporter and link your account to Discord.  

     2.1. You can obtain a token by clicking on `Get Token` in PogoDroid and sending the command `!settoken <your_token>` to the MAD Discord Bot.

3. Click "Get Refresh Token", then when you get to the next page it will tell you to copy a password and API Token.  Copy both, put them in a notepad (if you dont have a notepad app, nows the time to get one).  I think the API is not used, but still copy/paste both.  

4. On next screen login with the password they just gave you.  

5. Once logged in, click "Passwords" on the top.

6. On the password page it should tell you your Device Count allowed.  Below that it shows you the password for your phones.  If your adding a new phone, create a new password.  Copy that into a notepad.  Each phone needs its own password. Logout of this whole thing.

7. Go back to PogoDroid.  Use your email address and that new "Device Password" you setup in the previous step.

8. Now time to configure PogoDroid

**External Communication Section**
* -Disable external comm = Off
* -Post Destination = `http://ipofyourserver:8000`
* -Post Origin = Make this match what you put in RGC
* -Disable last sent notifications = On
* -Auth = Off

**Apps**
* -Broken: Repackage - don't touch
* -Export Settings - don't touch
* -Injection Delay - don't touch
* -Lower SELinux to permissive = On
* -Full daemon mode = On
* -Start Pogodoid with a delay (seconds) - don't touch
* -Enable OOm override = On
* -Test feature: Mock location patching = Off


## Final Steps

* Go into Android Settings, Security, Lock Screen Swipe, change to None.  You dont want a lock screen.  Locking and unlocking your phone should bring you right to the desktop.

* Turn on Airplane mode and make sure Wifi is still connected.

* Before we finish, go inside of Magisk and run the Safetynet Check one last time.  You need to see all green before proceeding.
