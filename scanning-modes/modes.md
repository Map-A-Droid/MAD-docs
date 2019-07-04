# OCR

OCR is short for "optical character recognition" and will take screenshots of the active raid tab. MAD will compare the little gym pictures with exsiting gym pictures in your Database.

# MITM

MITM is short for "man in the middle". PogoDroid will inject into the running Pokémon Go process to read out data.

## mon_mitm

`mon_mitm` will scan for Pokémon within a 70 meter radius. By default, no Pokémon gets encountered and checked for IV, but you can define a list (`mon_ids_iv`) of Pokémon IDs that should be encountered. The position of the IDs is the priority of them as well (So, for example, put Snorlax before Pidgey so PogoDroid will definetly scan Snorlax). The current limitation of PogoDroid is at two Pokémon at each location jump. 

## iv_mitm

This mode is relying on already scanned and active Pokémon in your DB (by `mon_mitm` for example) and will jump directly to them to do a IV check. `iv_mitm` will build up a "fist in first out" queue. 

## pokestops

You can use this mode for two things. Questscanning or leveling. Both requires the OCR stuff installed (python-pip packages, tesseract and opencv), no visible navigation bar (see [Phone Setup](http://https://mad-docs.readthedocs.io/en/latest/installation/phonesetup.html#final-steps)) and Magisk version 19 or lower.

Questscanning will walk on a route to every pokestop on the calculated route and spins it. When the area is set to `coords` in the walker, MAD will check every other stop in the area (even those who are not on the route) if they got scanned after the first round and will build a temporary route for them. This process will repeat itself three times. MAD is able to determinate the exact Pokémon encounter when picking up the quest.

The level option is basically the quest mode but without constantly clearing out the quests in the queststack and MAD will check if that stop is unique to that and will skip it if it's not. 

## raids_mitm

This mode is used to scan every gym and raid in a 480 meter radius. No interaction with any ingame objects is needed. MAD will only scan the gym color, the current gym defender, free Pokémon slots and the raid or egg if present. (More infos in the FAQ). 

## idle

The phone will stop Pokémon GO and do nothing.