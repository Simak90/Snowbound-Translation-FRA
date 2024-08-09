BL2 Snowbound Readme - Release v1.0.1

=========================
Readme Contents
=========================
1 - Important info
2 - Install instructions
3 - About the mod
4 - Known issues
5 - Credits



=========================
1 - Important info
=========================

If you read anything at all in this readme, please let it be this:

- This mod is single player only. Multiplayer does not work due to technical limitations.

- Sprinting has been disabled. Your default move speed is now faster than vanilla's sprint speed.

- The Challenges tab ingame is now a list of dedicated drop sources, indicating the amount of unique items they can drop.



=========================
2 - Install instructions
=========================

Note: This mod assumes you have all main DLCs installed (besides cosmetic DLCs or UHD texture pack). 
Not having certain DLCs may cause unintended behavior, such as not being able to use certain items.

1 - Install the Python SDK for BL2
  ~ Follow this guide here for more info: https://bl-sdk.github.io/
  
2 - Install the 'Snowbound' folder into your 'Mods' folder.
  ~ For Windows users on Steam, it will be located here:
	Program Files (x86)\Steam\steamapps\common\Borderlands 2\Binaries\Win32\Mods
	
3 - Ensure that cutscenes are enabled.
  ~ This is necessary to allow Constructor to generate new objects. You can check this in a couple of ways:
	In OpenBLCMM, open the Tools menu, then select Setup Game Files for Mods. Make sure Fewer Cutscenes is inactive.
	Or, in WillowEngine.ini (in Documents\My Games\Borderlands 2\WillowGame\Config), make sure bForceNoMovies=FALSE.
	Also, make sure you are not using the -NoMovies launch option on Steam.
	Note that this mod still skips cutscenes automatically.
	
4 - Enable the mod ingame in the Mods menu.
  ~ The mod will auto enable every time the game is launched until disabled again.

5 - Verify the mod is running.
  ~ Go to the challenges tab ingame. If you see yellow text at the bottom that says "Running SB + UCP", then you are all set.
    If not, see the Known Issues section down below.

Optional - Install Sanity Saver
  ~ Sanity Saver is useful for preventing item loss when loading a character without the mod active, and is highly recommended.
	Download Sanity Saver here: https://bl-sdk.github.io/mods/SanitySaver/

Optional - Check the optionals in OpenBLCMM.
  ~ In the 'Source' folder, opening the 'SB.blcm' file with OpenBLCMM will show optional categories that you can
	configure. Expand the category and select from the available options.
	Download OpenBLCMM here: https://github.com/BLCM/OpenBLCMM/releases

Compatibility with other mods is not guaranteed and may cause unintended behaviors.
To add other text mods to run alongside Snowbound, open SB.blcm in OpenBLCMM and click File > Import Mod Files.

To disable, toggle it in the in-game mod menu, then restart your game. To uninstall, remove the 'Snowbound' folder.



=========================
3 - About the mod
=========================

For a full list of features and changes, check the "Change List" file.

Main features of the mod include:
- 70+ brand new weapons and items.
- Reworked player movement speeds and air control.
- Allows the use of rockets, grenades, and other explosives to rocket jump.
- Reworks and stat tweaks for many skills and items.
- Improvments to all enemy stats and guns, as well as changes to enemy bullet speeds and visuals.
- Legendary rarity has been split into yellow and orange legendary. 
- Dark Magic elemental weapons return from Wonderlands.
- Unique weapons have a chance to become a hybrid weapon that grants the stats of another unique weapon.
- New alternate firing mode barrels can be found for common weapons.
- Improved boss battles, dedicated drop loot pools and drop chances.
- The "Challenges" tab ingame has been converted to the Codex, with info on boss locations, missions and drop types.
- More chests can be found across many of the base game maps.
- Quality of life and tons of other small tweaks.
- Lots of love and some sneaky secrets.



=========================
4 - Known issues
=========================

- Hotfixes sometimes do not apply properly (indicated by not having the "Running SB + UCP" text at the bottom of the challenges menu).
  ~ This is fixed by typing "exec Win32\Mods\Snowbound\Source\SB.blcm" into console, then save quitting once.
	If this occurs consistently, please reach out to me and let me know, as I am still investigating this further.

- Upon creating a new character, certain passive effects such as class abilities, dark magic status healing, and enemy speed may sometimes not be applied properly.
  ~ This is fixed by save quitting once, and only needs to be done once per character.
	Currently investigating further.

- Materials for modded items have their parent materials instead when loading in for the first time after launching the game.
  ~ This is fixed by re-equipping these items or by save quitting at least once. 
	Currently working on fixing.

- Weapons with modded parts in vendors will break when leaving and re-entering a map.
  ~ This is fixed by installing Sanity Saver and toggling the "Reroll Vendors on Level Transitions" option in the ingame mod options menu.
	
- Skags will sometimes do weird janky movements where they stutter forward repeatedly.
  ~ I am not sure how to fix this yet.
  
- After applying a dark magic status to an enemy, and then applying a slag status, the slag effects will not show visually on the enemy.
  Doing this vice versa will cause the slag effects to remain on the enemy until another slag status is applied. 
  ~ I am not sure how to fix this yet.
  
- The Trash Panda SMG can sometimes cause game crashes.
  ~ I am not sure how to fix this yet.

If you discover any issues, please post it on the Nexus mod page, or feel free to message me on Discord at: dr.bones
(Please do not ask for installation help)



=========================
5 - Credits
=========================

Snowbound made by Dr. Bones
Constructor made by Juso

This mod uses the following mods with each respective author's permission:
Unofficial Community Patch 5 (by Shadowevil and the UCP team)
Fast Travel Portal Disabler (by FromDarkHell)
Respawning Enemies and Allies (by Our Lord & Savior Gabe Newell)
No More Enemy Bullet Reflection (by Aaron0000)
Vendors Enhanced (by Kuma, Jim Raven, and the_Nocturni)
BL2 Mega TimeSaver XL (by Apocalyptech and Gronp)
Manufacturer Sorted Vending Machines (by Our Lord & Savior Gabe Newell)
BL2 Early Bloomer (by Apocalyptech)
Remove Level Variance (from BL2 Reborn, by Kuma)
Thanks to ZetaDaemon, for various fixes

Additional thanks to the streamers who played live on Twitch during the Open Beta period: 
Shadowevil, Pawn, WholyMilk.

Additional thanks to the many Open Beta feedback contributors: 
Zazk, Rapoulas, Shiroe, Elbow Removal Service, Joto, Hypergrad22, TheBus, Jeff, 
CrusaderOfSpeed, Nemo, MiniDarTooNz, CheshireKaz, Bacooba, Chordking223, Salt, 
Buddy, Lilu, Unb, Junu, Sartick, Machers.

And thank you! For playing this mod <3

Chaaaiiins! Follow me! https://www.youtube.com/@Bonelord69