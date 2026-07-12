"""
steam data
"""

from src.classes.game_data import GameData


class SteamData(GameData):
    def __init__(self) -> None:
        self.appid:str = ""  # steam app id
