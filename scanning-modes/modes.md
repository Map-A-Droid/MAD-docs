# MITM

MITM is short for "Man In The Middle". PogoDroid will inject into the running game process to read the data which is received from the game server.

## mon_mitm

`mon_mitm` will scan for mon within a 70 meter radius. By default, no mon gets encountered and checked for IV, unless you define a list (`mon_ids_iv`) of IDs that should be encountered. The order of the IDs is the priority of them. So, for example, put Snorlax before Pidgey to make sure PogoDroid will scan Snorlax first). PogoDroid has a built-in limit of 2 encounter per location.

## iv_mitm

This mode is relying on already scanned and active mon in your DB (via `mon_mitm` for example). It will jump directly to them to do an IV check. `iv_mitm` will build up a "first in first out" queue.

## pokestops

You can use this mode for two things. Quest scanning or leveling. Both require the OCR requirements being installed (python-pip packages, tesseract and opencv), no visible navigation bar (see [Phone Setup](http://https://mad-docs.readthedocs.io/en/latest/installation/phonesetup.html#final-steps)) and Magisk prior version 19.1. Magisk 19.1 and above won't work!

Quest scanning will walk on a pre-calculated route to every stop and spin it. When the area is set to `coords` in the walker, MAD will check every other stop in the area (even those who are not on the route). Those stops will be processed after the first round. This process will repeat itself three times. MAD is able to determinate the exact mon encounter and item type when picking up the quest.

The level option is basically the quest mode but without constantly clearing out the quests in the queststack and MAD will check if that stop is unique for the worker. In case it's a stop that has been visited in the past, it will be skipped.

## raids_mitm

This mode is used to scan every gym and raid in a 490 meter radius. No interaction with any ingame objects is needed. MAD will only scan the gym color, the current gym defender, free slots and the raid or egg if present. (More about that in the FAQ).

## idle

The phone will stop the game and do nothing.
