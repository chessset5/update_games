"""
functions for steam
"""

from pathlib import Path, WindowsPath
from src.classes.steam_data import SteamData
from src.helpers.getGames.helpers.get_exe import get_exes
from typing import cast
from src import STEAM


# Default Paths
STEAM_APPS: Path = WindowsPath(r"C:\Program Files (x86)\Steam\steamapps")
STEAM_GAMES_FOLDER: Path = STEAM_APPS / "common"


def parse_game(file: Path) -> dict[str, str]:
    data = dict()
    with open(file=file, mode="r", encoding="utf-8") as rf:
        for line in rf.readlines():
            line: str = line.strip()
            for target in ['"appid"', '"name"', '"installdir"']:
                if target in line:
                    key, value = line.split(maxsplit=1)
                    key = key.strip('"')
                    value = value.strip('"')
                    data[key] = value
    return data


def get_games() -> list[SteamData]:
    """
    returns all the games and paths in steam
    """
    game_files: list[Path] = [i for i in STEAM_APPS.iterdir() if i.suffix == ".acf"]

    data: list[SteamData] = []

    for gf in game_files:
        game_data: dict[str, str] = parse_game(gf)
        if game_data["name"] != "Steamworks Common Redistributables":
            d = SteamData()
            d.service = STEAM
            d.name = game_data["name"]
            d.appid = game_data["appid"]
            d.dir = STEAM_GAMES_FOLDER / game_data["installdir"]

            exe: list[Path] = get_exes(d.dir)
            d.locations = cast(list[Path | str], exe)

            data.append(d)
    return data
