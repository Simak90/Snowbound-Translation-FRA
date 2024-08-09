import unrealsdk
from unrealsdk import *

from ..ModMenu import SDKMod, EnabledSaveType

import os
import re
from configparser import ConfigParser

from . import logging, hookmanager, assignor, constructor, hotfix_manager, spawner
from . import custompawns as pawns
from . import matinstconsts as mat
from . import bl2pysave as pysave
from . import bl2tools

class ConstructorMain(SDKMod):
    Name = "Snowbound"
    Version = "1.0.1"
    Description = "Snowbound mod for Borderlands 2. Made with Juso's Constructor. \n\nSnowbound is a full game overhaul focused on fast paced, fluid combat. Experience BL2 as an old school run-and-gun style shooter with fundamental changes to movement and gunplay. Featuring 70+ brand new items, reworked uniques, dark magic elemental, more chests, tougher bosses, hybrids, and tons more. Did I mention rocket jumping?"
    Author = "Dr. Bones"
    Types = unrealsdk.ModTypes.Content
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu


    def __init__(self):
        self.ini_works = ConstructorMain.check_willow_engine_ini()
        self.FILE_PATH = os.path.dirname(os.path.realpath(__file__))
        self.config = ConfigParser(comment_prefixes="/", allow_no_value=True)
        self.config.read(os.path.join(self.FILE_PATH, "settings.ini"))
        if self.config.getboolean("main", "optimize_on_startup"):
            self.config.set("main", "optimize_on_startup", "false")
            with open(os.path.join(self.FILE_PATH, "settings.ini"), "w") as f:
                self.config.write(f)
            ConstructorMain.optimize()

        logging.logger = logging.Logger(self.config.get("main", "log_level").strip(),
                                        self.config.getboolean("main", "log_all_calls", fallback=False))

        self.Constructor = constructor.Constructor(self.FILE_PATH)
        self.HotfixMan = hotfix_manager.Hotfixer(self.FILE_PATH)
        self.Pawns = pawns.Pawns(self.FILE_PATH)
        self.Saves = pysave.PySave(self.FILE_PATH)
        self.Assignor = assignor.Assignor(self.FILE_PATH)
        self.Materials = mat.Materials(self.FILE_PATH)
        self.Spawner = spawner.Spawner(self.FILE_PATH)
        self.initial_spawn = True

    def passive_skill_trigger(self):
        player_skills = {
            "GD_Soldier.Character.CharClass_Soldier": [
                "GD_Soldier_Skills.Gunpowder.SB_Skill_Soldier",
            ],
            "GD_Mercenary.Character.CharClass_Mercenary": [
                "GD_Mercenary_Skills.Rampage.SB_Skill_Merc",
            ],
            "GD_Assassin.Character.CharClass_Assassin": [
                "GD_Assassin_Skills.Cunning.SB_Skill_Assassin",
            ],
            "GD_Siren.Character.CharClass_Siren": [
                "GD_Siren_Skills.Harmony.SB_Skill_Siren",
            ],
            "GD_Tulip_Mechromancer.Character.CharClass_Mechromancer": [
                "GD_Tulip_Mechromancer_Skills.EmbraceChaos.SB_Skill_Mechro",
            ],
            "GD_Lilac_PlayerClass.Character.CharClass_LilacPlayerClass": [
                "GD_Lilac_Skills_Mania.Skills.SB_Skill_Psycho",
            ]
        }
        def activate_passive_skill(this: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            PC = unrealsdk.GetEngine().GamePlayers[0].Actor
            SM = PC.GetSkillManager()
            for klass, skills in player_skills.items():
                if PC.PathName(PC.PlayerClass) != klass:
                    continue
            for s in skills:
                skill = unrealsdk.FindObject("SkillDefinition", s)
                if not SM.IsSkillActive(PC, skill):
                    SM.ActivateSkill(PC, skill)
            return True
        unrealsdk.RegisterHook("Engine.GameInfo.PostCommitMapChange","PassiveSkillTrigger",activate_passive_skill)
    

    def Enable(self) -> None:
        if not self.ini_works:
            pc = bl2tools.get_player_controller()
            pc.GFxUIManager.ShowTrainingDialog(
                "Documents>My Games>Borderlands 2>WillowGame>Config>WillowEngine.ini Please Change "
                "bForceNoMovies=TRUE to bForceNoMovies=FALSE.\nIf you do not change it, this mod won't work. Make sure "
                "to restart the game after making these changes.",
                "Note", 10)
            raise Exception("Won't enable SB with bForceNoMovies .ini Tweak!")

        self.Constructor.Enable()
        self.HotfixMan.Enable()
        self.Pawns.Enable()
        self.Materials.Enable()
        self.Saves.Enable()
        self.Assignor.Enable()
        self.Spawner.Enable()
        hookmanager.instance.Enable()
        logging.logger.info(f"Everything setup and ready to play")
        if not self.config.getboolean("main", "has_seen_version_notes"):
            self.config.set("main", "has_seen_version_notes", "true")
            with open(os.path.join(self.FILE_PATH, "settings.ini"), "w") as f:
                self.config.write(f)
            self.show_version_notes()
        def begin_execute(this: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            self.AID.SetBaseValue(self.accel_rate, (2048, None, None, 1), this.MyWillowPawn, this.MyWillowPawn)
            this.BeginExecute()
            unrealsdk.Log('exec begin')
            return False


        def end_execute(this: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            this.RestorePhysicsPostExecute()
            self.AID.SetBaseValue(self.accel_rate, (2048, None, None, 1), this.MyWillowPawn, this.MyWillowPawn)
            unrealsdk.Log('exec end')
            return False

        self.accel_rate = unrealsdk.FindObject("AttributeDefinition", "D_Attributes.Movement.AccelRate")
        self.AID = unrealsdk.FindObject("AttributeInitializationDefinition", "Engine.Default__AttributeInitializationDefinition")
    
        unrealsdk.RegisterHook("WillowGame.ExecuteActionSkill.BeginExecute", "snowbound_ex_begin", begin_execute)
        unrealsdk.RegisterHook("WillowGame.ExecuteActionSkill.RestorePhysicsPostExecute", "snowbound_ex_end", end_execute)
    
        def init_spawn(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if self.initial_spawn:
                pc = bl2tools.get_player_controller()
                if pc is not None:
                    hud = pc.GetHUDMovie()
                    if hud is not None:
                        self.initial_spawn = False
                        hud.ClearTrainingText()
                        hud.AddTrainingText(" \n"
                                            "Thanks for playing, and have fun!",
                                            f"Snowbound {self.Version} Is Running",
                                            8.000000, (), "", False, 0,
                                            pc.PlayerReplicationInfo, True)
            return True

        self.passive_skill_trigger()
        unrealsdk.RegisterHook("WillowGame.WillowHUD.CreateWeaponScopeMovie", "ConstructorRunningMsg", init_spawn)

    def Disable(self) -> None:
        pc = bl2tools.get_player_controller()
        pc.GFxUIManager.ShowTrainingDialog(
            f"If you are trying to disable {self.Name}, this is only possible by closing your game.\n"
            f"This is due to too many changes that cannot be reverted.",
            "Disable", 5)
        unrealsdk.RemoveHook("Engine.GameInfo.PostCommitMapChange","PassiveSkillTrigger")

    @staticmethod
    def optimize() -> None:
        path = os.path.dirname(os.path.realpath(__file__))
        for extension in (".construct", ".loaded", ".mission", ".itempool", ".assign",
                          ".set", ".lootable", ".reward", ".material", ".popdef", ".pawn", ".spawn"):
            with open(os.path.join(path, "src", f"MASTER{extension}"), "w", encoding="cp1252") as master_file:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.split(".")[0] == "MASTER":
                            continue
                        if file.lower().endswith(extension):
                            with open(os.path.join(root, file), encoding="cp1252") as f:
                                for line in f:
                                    if not line.rstrip():
                                        continue
                                    if line.lstrip()[0] != "-":
                                        master_file.write(f"{line.rstrip()}\n")
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file == f"MASTER{extension}":
                        continue
                    if file.lower().endswith(extension):
                        os.remove(os.path.join(root, file))
        hfiles = []
        keys = []
        vals = []
        for root, dirs, filenames in os.walk(path):
            for file in filenames:
                # .definition as alternative suffix support for Exodus
                if file.lower().endswith(".definition") or file.lower().endswith(".blcm"):
                    hfiles.append(os.path.join(root, file))
        SparkServiceConfiguration = None
        set_cmd = "set {} {} ({})\n"
        with open(os.path.join(path, "src", "MASTER.definition"), "w", encoding="cp1252") as merge_fp:
            for file in hfiles:
                with open(file, "r", encoding="cp1252") as fp:
                    for line in fp:
                        if line.lstrip().lower().startswith("set"):
                            if "SparkService" not in line:
                                merge_fp.write(line)
                            else:
                                _split = line.split(maxsplit=3)
                                attr = _split[2]  # set0 Object1 attribute2 value3:
                                to_merge = _split[3].rstrip()
                                if attr.lower() == "keys":
                                    keys.append(to_merge[1:-1])
                                elif attr.lower() == "values":
                                    vals.append(to_merge[1:-1])

            for x in unrealsdk.FindAll("SparkServiceConfiguration"):
                if x.ServiceName == "Micropatch":
                    SparkServiceConfiguration = x.PathName(x)
                    break
            if not SparkServiceConfiguration:
                SparkServiceConfiguration = "Transient.SparkServiceConfiguration_0"
                merge_fp.write("set Transient.SparkServiceConfiguration_0 ServiceName Micropatch\n")
                merge_fp.write("set Transient.SparkServiceConfiguration_0 ConfigurationGroup Default\n")
                gb_acc = unrealsdk.FindAll("GearboxAccountData")[-1]
                merge_fp.write(
                    "set {} Services (Transient.SparkServiceConfiguration_0)\n".format(gb_acc.PathName(gb_acc)))

            # remove double gearbox hotfixes
            all_keys = ",".join(keys)
            all_vals = ",".join(vals)

            pat = re.compile(r"\"([^\"\\]*(?:\\.[^\"\\]*)*)\"")

            gbx_keys = set()
            gbx_vals = set()
            own_keys = list()
            own_vals = list()
            for k, v in zip(re.findall(pat, all_keys), re.findall(pat, all_vals)):
                if k not in gbx_keys:
                    own_keys.append(f"\"{k}\"")
                    own_vals.append(f"\"{v}\"")
                if "gbx_fixes" in k.lower():  # filter out all duplicate gbx hotfixes
                    gbx_keys.add(k)
                    gbx_vals.add(v)

            merge_fp.write(set_cmd.format(SparkServiceConfiguration, "Keys", ",".join(own_keys)))
            merge_fp.write(set_cmd.format(SparkServiceConfiguration, "Values", ",".join(own_vals)))

        for f in hfiles:
            os.remove(f)

    def show_version_notes(self) -> None:
        pc = bl2tools.get_player_controller()
        version_notes = f"<font color=\"#A83232\">Important Info!</font>\n" \
                        f"- This mod is single player only. Multiplayer does not work due to technical limitations.\n" \
                        f"- Sprinting has been disabled. Your default move speed is now faster than vanilla's sprint speed.\n" \
                        f"- The Challenges tab ingame is now a list of dedicated drop sources, indicating the amount of unique items they can drop.\n" \
                        f"\n" \
                        f"Please read the Readme file for more details.\n" \
                        f"Thanks for playing, and have fun!" \

        title = f"{self.Name} v.{self.Version} Info"
        pc.GFxUIManager.ShowTrainingDialog(version_notes, title, 4)

    @staticmethod
    def check_willow_engine_ini() -> bool:
        ini_path = os.path.join(os.path.expanduser("~"), "Documents", "my games", "Borderlands 2", "WillowGame",
                                "Config")
        try:
            with open(os.path.join(ini_path, "WillowEngine.ini"), "r") as f:
                for line in f:
                    if "bforcenomovies=true" in line.lower():
                        return False
            return True
        except Exception as e:
            unrealsdk.Log(e)
            return True
    

if __name__.startswith("Mods"):
    unrealsdk.RegisterMod(ConstructorMain())
