"""
default class for game data

"""

from pathlib import Path


class GameData:
    def __init__(self) -> None:
        self.name: str = ""  # name of the game
        self.locations: list[str | Path] = [] # location of the exe, can have multiple paths for multiple verisons
        self.dir: str | Path = ""  # directory of the game
        self.service: str = ""  # service that has the game, ie Steam, Epic, Uplay, etc
