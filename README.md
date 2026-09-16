# Archipelago-POPWW

This is the repository for the Prince of Persia Warrior Within Archipelago implementation.
Please keep in mind that this is an early version of the code, I am currently learning how to create a .apworld file as I am creating this one. This means that code may not be functional, the structure may be subject to major changes because I don't have a global idea of what I need to put in the files.
This serves as a way to show the progress and potentially get feedback. If you have any ideas, feel free to put them in the discord channel on the official Archipelago community server.
The final goal is to create a mod that you will install in the game files so it will be automatic.
It will be developed for the pc version first (Steam version will be used but other pc versions should be compatible), with the possibility of adapting the apworld and mod for the psp port.


Here are the Rules I imagined:

The goal is to either kill the Empress or the Dahaka, based on what you choose (will be an option when creating the yaml file)

Locations: 
- Every Primary Sword, Health Upgrade, Sand Power unlock/upgrade will constitute a location.
- Every hidden artwork chest constitutes a location
- Every first secondary weapon pickup constitutes a location
- Defeating major Bosses constitutes a check. The following are currently considered as locations: Shahdee, Kaileena (first time), Griffin, Kaileena/Dahaka (win condition)
- The Mask of the Sandwraith

Items:
- Every Primary Sword (progressive sword)
- Health Upgrades (8 or 9 depending on your goal, as putting 9 if you chose Kaileena would potentially lock you)
- Sand Powers
- Secondary Weapons
- The Mask of the Sandwraith
- Kaileena's sword/Shahdee's sword (secret items, not obtainable without modifying the game's memory, but the mod will do it so let's include them)

If you do not like certain options or think I missed some, feel free to tell me. Some things could be put as a choice (for instance if you don't want to track every secondary weapon)
Also, the classification of items isn't set in stone. Swords will be progressive items, but only the Eye of the Storm (slowing down time) is considered progressive among the sand powers as it is the only one actually required to complete the game. Still, I'm thinking of changing this to include the Recall and Sand Containers, as they are above useful. Secondary weapons are considered Usefeul, but I might put only the strongest ones in that category as useful and the others as filler checks. I know that I will have to be careful about sending weapons and using said weapons pickup as locations. Perhaps you'll only be allowed to receive weapons you've already found, let me know what you think about it.

Roadmap:
The goal is to first get a prototype working with the features mentioned above. I will try to add the following features to following versions. Some of them are just ideas and might be undoable:
- The boat section can have checks through weapons, I will try to include it later through a level loader so you can get them. At first, I will try to skip it as it can't be accessed again in a normal playthrough.
- HD texture support. I know many people play with enhanced textures, but this is not the priority in my opinion. The prototype version might still work with HD textures, or perhaps not. Either way, I will try to look into it after the first prototype launches.
- Teleportation points as some areas can only be accessed once in a normal playthrough (Cliff or Mystic Caves for instance) and have one way connections to other areas, meaning if you miss a location in there you're toast. I hope that only veteran players will test it at first and won't miss them. This could also fix the infamous bug of the gate after the sacrificial altar. If you backtrack to the sacrificial altar, a gate that was destroyed is back up and you're softlocked, I want to prevent that.
- Possibility to start from different locations, might be very tough because of the logic of the game, don't count on it too much
- Random room connectivity? Would it even be possible? I'm writing whatever I can think of, regardless of whether they're good ideas.
