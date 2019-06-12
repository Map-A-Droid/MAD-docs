# FAQ

## General

### How many Pokémon/Quests/Raids can i scan with one device?

Noone can tell that. That's depending on your Area. How many spawnpoints/pokestops/gyms are in that area and how far is the distance between them. Start with a small area, increase it over the time and see how much is possible.

### Is a function to see gym defenders and trainernames planed?

No. Definetly not. To avoid drama *and* privacy concerns the MAD developers decided not to code such a feature.

## MAD

### All my Pokestop and Gym names are `unknown`

Pogodroid don't fetch those names and pics automatically in init mode. You can ether run questmode to get the Pokestop names and/or use the [intelimport.sh](https://mad-docs.readthedocs.io/en/latest/extras/scripts.html#intel-importer-intelimport-sh) script to import those names and pictures from Ingress.

### How can i check if my MAD receives data?

If you see a green line with `Processing GMO` in it, then leave it alone - it's working

### Madmin has missing images

Check your `pogoasset` config in `config.ini` and use a full path (starting with `/` on Linux) instead of a relative path.

## Pokémon Go

### My character is stuck in the ocean and its not moving

If you dont have a red GPS at the top that means that RGC is working but didn't got any commands from your MAD server.

- Check if your phone registered to your MAD server. The log line should look like this: `[scanner] [    WebsocketServer:134 ] [    INFO] Client ORIGINNAME registering`
- Check if that phone has something to do according to your mappings. Have a look at your MAD logs for that.

### Pogo (sometimes) says that my phone has an unsupported OS

Sometimes it may just be a hickup, try a reboot

- Check safetynet status: [https://play.google.com/store/apps/details?id=com.scottyab.safetynet.sample](https://play.google.com/store/apps/details?id=com.scottyab.safetynet.sample) your phone has to pass that check.
- Go into MagiskManager and repackage it if you have not done so already: MagiskManager->Setting ->Repackage MagiskManager
- Add pogo to the list of Magisk Hide: MagiskManager->Magisk Hide-> Check Pogo

### I can see the red error (70) sometimes

That's nothing to worry about. It's the way Pogodroid can scan IV.

### Questmode dont click anything on the screen

- Check if you are using a correct Magisk version. 19.1, 19.2 and sometimes 19.3 blocking RGC to click on the screen.
- Check if you have a [navigation bar](https://material.io/design/platform-guidance/android-bars.html#android-navigation-bar) on your screen. If yes: disable it with this adb command: `adb shell settings put global policy_control immersive.full=com.nianticlabs.pokemongo`
