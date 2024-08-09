from typing import Callable, List, Tuple

import unrealsdk
from unrealsdk import *

from . import logging

import random

__all__ = ["instance"]


class HookManager:

    def __init__(self):
        self.call_order_end_load: List[Tuple[int, Callable[[str], None]]] = []
        self.call_order_start_load: List[Tuple[int, Callable[[str], None]]] = []
        self.b_add_default_motd: bool = False
        self.motds = [
            ("Snowbound", "Thanks for playing, and have fun!", 7),

        ]

    def Enable(self) -> None:
        self.call_order_end_load.sort()
        self.call_order_start_load.sort()

        def EndLoad(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            curr_map = unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower()
            logging.logger.debug(f"Loaded map: {curr_map}")
            for _, func in self.call_order_end_load:
                try:
                    func(curr_map)
                except Exception as e:
                    logging.logger.error(repr(e))
                    logging.logger.error(f"Something went wrong on ClientDisableLoadingMovie in {func}!")
            return True

        def StartLoading(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if params.MovieName is None:
                return True
            logging.logger.debug(f"Loading map: {params.MovieName}")
            for _, func in self.call_order_start_load:
                try:
                    func(params.MovieName)
                except Exception as e:
                    logging.logger.error(repr(e))
                    logging.logger.error(f"Something went wrong on ClientShowLoadingMovie in {func}!")
            return True

        def show_motd(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if self.b_add_default_motd:
                for motd in caller.MessagesOfTheDay:
                    self.motds.append((motd.Header, motd.Body, 4))
                random.shuffle(self.motds)
                self.b_add_default_motd = False
            caller.MessagesOfTheDay = self.motds
            return True

        def close_motd(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            caller.MessagesOfTheDay = []
            return True

        def get_motd(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            return False

        unrealsdk.RegisterHook("WillowGame.FrontendGFxMovie.ShowMOTD", "MotD", show_motd)
        unrealsdk.RegisterHook("WillowGame.FrontendGFxMovie.OnClose", "OnClose", close_motd)
        unrealsdk.RegisterHook("WillowGame.FrontendGFxMovie.GetMessageOfTheDay", "get_motd", get_motd)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie",
                               "hkManagerEndLoading",
                               EndLoad)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie",
                               "hkManagerStartLoading",
                               StartLoading)

    def Disable(self) -> None:
        pass

    def register_end_load(self, fnc: Callable[[str], None], priority: int) -> None:
        """

        :param fnc: function to be called at each end of map load, function needs to take 1 str param, current map name
        :param priority: lower means called earlier
        :return:
        """
        self.call_order_end_load.append((priority, fnc))

    def register_start_load(self, fnc: Callable[[str], None], priority: int) -> None:
        """

        :param fnc: function to be called at each start of map load, function needs to take 1 str param, current map
        name
        :param priority: lower means called earlier
        :return:
        """
        self.call_order_start_load.append((priority, fnc))


instance = HookManager()
