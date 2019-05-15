## How does MAD work?
MAD is a system to collect Data from Pokémon GO. It uses real Android smartphones and processes the data into a database. MAD is currently able to scan for Raids, Quests, Pokémon and its IVs. 
>Note: Quests and Pokémon are only possible with the MITM method

### Android phone
The phone needs to be rooted, pass the [SafetyNet Check](https://koz.io/inside-safetynet/) and SELinux  must be permissive or moderate. In the most cases rooting with Magisk solves all those problems.

#### Remote GPS Controller (RGC)
RGC is an app developed by the MAD team to control the phone in various ways. It handles the GPS spoofing, takes screenshots, restarts Pokémon GO, reboots the whole phone and more. This app is necessary for MAD. 

#### Pogodroid
This app injects into the running Pokémon GO process and relays the [Protos](https://github.com/Furtif/POGOProtos) sent to Pokémon GO to the MAD server. Pogodroid is only required when using the MITM method. A valid token is required to use it, you can purchase it on [the MAD website](https://www.maddev.de/).

### MAD server
MAD is a python application, so its able to run on Linux, Windows and Mac OS. It was developed on Linux only and no one can guarantee that it runs perfectly on other operating systems. We highly suggest to setup a Linux Virtual Machine when no native Linux is present.

![](_static/concept.jpg)
