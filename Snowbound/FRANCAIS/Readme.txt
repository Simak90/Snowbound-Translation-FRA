BL2 Snowbound Readme - Release v1.0.1

===============================
Sommaire du fichier
===============================
1 - Infos importantes
2 - Instructions d'installation
3 - À propos du mod
4 - Problèmes connus
5 - Crédits



===============================
1 - Infos importantes
===============================

Si vous devriez lire quoi que ce soit dans ce readme, ce serait ça:

- Ce mod n'est jouable qu'en solo. Le multijoueur ne marchera pas à cause de limitations techniques.

- Le sprint est désactivé. La vitesse de marche est maintenant plus rapide que la vitesse de sprint en vanilla.

- L'onglet "Défis" est remplacé par une liste de sources de loot dédié, indiquant le nombre d'items uniques qu'ils peuvent drop.



===============================
2 - Instructions d'installation
===============================

Note: Ce mod suppose que vous avez tous les DLCs principaux installés (en dehors des skins ou du texture pack UHD)
Ne pas être en possession de certains DLCs peut causer des comportements non voulus, comme l'incapacité à utiliser certains objets.

1 - Installez Python SDK pour BL2.
  ~ Suivez ce guide ci-joint pour plus d'info: https://bl-sdk.github.io/

2 - Déplacez le dossier "Snowbound" dans votre dossier "Mods".
  ~ Pour les utilisateurs Windows sur Steam, l'emplacement sera:
    Si Borderlands 2 est sur le même disque que Steam : Program Files (x86)\Steam\steamapps\common\Borderlands 2\Binaries\Win32\Mods
    Si Borderlands 2 n'est pas sur le même disque que Steam : SteamLibrary\steamapps\common\Borderlands 2\Binaries\Win32\Mods

3 - Assurez-vous que les cinématiques sont activées.
  ~ Cette partie est nécessaire pour permettre au Constructeur de générer de nouveaux objets. Vous pouvez vérifiez cela de différentes façons:
  Dans OpenBLCMM, ouvre le menu Tools, et sélectionnez "Setup Game Files for Mods". Vérifiez si l'option "Fewer Cutscenes" est bien désactivée.
  Ou bien, dans WillowEngine.ini (dans Documents\My Games\Borderlands 2\WillowGame\Config), assurez-vous que bForceNoMovies=FALSE.
  Ensuite, assurez-vous de ne pas utiliser l'option de lancement -NoMovies sur Steam.
  À noter que ce mod va par lui-même sauter les cinématiques.

4 - Activez le mod en jeu via le menu "Mods".
  ~ Le mod va s'activer automatiquement à chaque ouverture du jeu jusqu'à ce qu'il soit désactivé.

5 - Vérifiez que le mod tourne.
  ~ Allez dans l'onglet des Défis en jeu. Si vous voyez un texte jaune en bas qui dit "SB + UCP en exécution", alors tout est bon.
    Sinon, allez voir la section "4 - Problèmes connus" de ce document.

Optionnel - Installez "Sanity Saver"
  ~ Sanity Saver est utile pour éviter la perte d'items quand on charge un personnage sans que le mod soit activé, et est par conséquent vivement recommandé.
  Téléchargez Sanity Saver ici: https://bl-sdk.github.io/mods/SanitySaver/

Optionnel - Modulez les options que vous voulez dans OpenBLCMM.
  ~ Dans le dossier "Source", ouvrir le fichier "SB.blcm" avec OpenBLCMM montrera des options que vous pourrez configurer. Déroulez simplement la catégorie "Optionnel" et sélectionnez les options que vous souhaitez.
  Téléchargez OpenBLCMM ici: https://github.com/BLCM/OpenBLCMM/releases

La compatibilité avec d'autres mods n'est pas garantie et peut causer des comportements non voulus.
Pour ajouter d'autres mods avec Snowbound, ouvrez SB.blcm dans OpenBLCMM et appuyez sur File > Import Mod Files.

Pour désactiver le mod, désactivez-le dans le menu "Mods", puis redémarrez votre jeu. Pour le désinstaller, supprimez le dossier "Snowbound" du dossier "Mods".



===============================
3 - À propos du mod
===============================

Pour une liste exhaustive des nouvelles fonctionnalités et des changements, veuillez consulter le fichier "Change List.txt".

Les principales nouveautés du mods sont:
- 70+ nouvelles armes et objets.
- Refonte de la vitesse de déplacement du joueur et des mouvements dans l'air.
- Permet l'utilisation de roquettes, grenades, et bien d'autres explosions pour le saut. -- Préféré du traducteur : LA BUZZAXE EXPLOSIVE DE KRIEEEEEEEEEG
- Refonte et modulation des stats pour beaucoup de compétences et d'objets.
- Améliorations des stats des ennemis et des armes, complémenté par des changements sur les visuels et la vitese des balles ennemies.
- La rareté Légendaire a été divisée en légendaire jaune et légendaire orange.
- L'élément de Magie noire des Wonderlands fait son apparition.
- Les armes uniques ont une chance de devenir des armes hybrides qui octroient les stats d'une autre arme unique.
- D'autres canons de tirs peuvent être trouvés sur les armes à faible rareté.
- Combats de boss améliorés, en plus d'une revalorisation du loot dédié et de son taux de drop.
- L'onglet "Défis" a été converti en "Codex", avec des infos sur l'emplacement des boss, des missions et des types de drops.
- Plein de coffres ont été parsemés dans les maps du jeu de base.
- Des changements de QoL et d'autres petits tweaks.
- Plein d'amour et d'autres secrets dissimulés.



===============================
4 - Problèmes connus
===============================

- Les hotfix ne s'appliquent pas toujours dûment (indiqué par le fait de ne pas avoir le message "SB + UCP en exécution" en bas de l'onglet Défis)
  ~ Ça se répare en écrivant "exec Win32\Mods\Snowbound\Source\SB.blcm" en quittant puis revenant dans la partie
  Si cela arrive fréquemment, je vous prie de me contacter pour me le faire savoir, car je suis toujours en train de travailler dessus.

- À la création d'un nouveau personnage, certains passifs comme les compétences de classe, la régénération via Magie noire, et la vitesse des ennemis peuvent des fois ne pas marcher correctement.
  ~ Ça se répare en quittant puis revenant dans la partie, et ça n'a besoin que d'être fait une fois par personnage.
  En train d'enquêter dessus en profondeur.

- Les matériaux pour les objets moddés ont à la place des matériaux qui leur sont parents quand on lance la partie après avoir lancé le jeu.
  ~ Ça se répare en déséquippant/ré-équippant ces objets ou en quittant puis revenant dans la partie au moins une fois.
  En train de travailler sur un correctif.

- Les armes avec des composants moddés sont cassés quand on change de map.
  ~ Ça se répare en installant Sanity Saver et en activant l'option "Reroll Vendors on Level Transitions" dans le menu "Mod Options" en jeu.

- Des fois, les skags font des mouvements bizarres et font des arrêts au hasard;
  ~ Je ne suis pas sûr de comment réparer ça pour l'instant.

- Après avoir appliqué l'effet de statut Magie noire à un ennemi, en appliquant un statut de slag, les effets du slag ne seront pas affichés sur l'ennemi.
  Répétant ce processus à l'envers fait en sorte que les effets du slag restent sur l'ennemi jusqu'à ce qu'un autre statut de slag ne soit appliqué.
  ~ Je ne suis pas sûr de comment réparer ça pour l'instant.

- La mitraillette Trash Panda peut causer des crashs.
  ~ Je ne suis pas sûr de comment réparer ça pour l'instant.

Si vous découvrez d'autres soucis, je vous remercie de les signaler en commentant sur la page du mod sur Nexus, ou bien de me contacter sur Discord: dr.bones
(S'il-vous-plaît ne demandez pas de l'aide sur l'installation du mod)



===============================
5 - Crédits
===============================

Snowbound créé par Dr. Bones
Constructor créé par Juso

Ce mod utilise les mods suivants avec la permission de leur auteur respectif:
Unofficial Community Patch 5 (par Shadowevil et the UCP team)
Fast Travel Portal Disabler (par FromDarkHell)
Respawning Enemies et Allies (par Our Lord & Savior Gabe Newell)
No More Enemy Bullet Reflection (par Aaron0000)
Vendors Enhanced (par Kuma, Jim Raven et the_Nocturni)
BL2 Mega TimeSaver XL (par Apocalyptech et Gronp)
Manufacturer Sorted Vending Machines (par Our Lord & Savior Gabe Newell)
BL2 Early Bloomer (par Apocalyptech)
Remove Level Variance (de BL2 Reborn, par Kuma)
Merci à ZetaDaemon pour ses différents correctifs

Un merci aussi aux streamers qui y ont joué en live pendant la période de Bêta Ouverte:
Shadowevil, Pawn, Wholymilk.

Un autre merci pour les nombreux contributeurs à l'avancée durant la période de Bêta Ouverte:
Zazk, Rapoulas, Shiroe, Elbow Removal Service, Joto, Hypergrad22, TheBus, Jeff, 
CrusaderOfSpeed, Nemo, MiniDarTooNz, CheshireKaz, Bacooba, Chordking223, Salt, 
Buddy, Lilu, Unb, Junu, Sartick, Machers.

Et merci à vous! Merci de jouer à ce mod <3

Chaaaiiins! Follow me! https://www.youtube.com/@Bonelord69 -- non traduit car c'est l'essence du gars 😊