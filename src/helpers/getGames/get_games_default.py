"""
functions for most games

This will work for most game services
"""

from pathlib import Path, WindowsPath
from src.classes.game_data import GameData
from src.helpers.getGames.helpers.get_exe import get_exes
from typing import cast


def get_games(root: Path, service: str) -> list[GameData]:
    """
    returns all the games and paths in the given folder
    """
    game_folder: list[Path] = [i for i in root.iterdir() if i.is_dir()]

    data: list[GameData] = []

    for gf in game_folder:
        exes: list[str | Path] = cast(list[str | Path], get_exes(gf))
        if exes:
            game_data = GameData()
            game_data.name = gf.name
            game_data.locations = exes
            game_data.dir = gf
            game_data.service = service
    return data
