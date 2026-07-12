from pathlib import Path
from src import WORKSPACE, DATA_FOLDER, CONFIG_FOLDER
from src.helpers.getGames.steam import get_games as get_steam_games


def get_games() -> dict[str, list]:
    return {"steam": get_steam_games()}


def main():
    # setup one:
    # common games folders:
    #   steam
    #   epic
    #   Ubisoft
    #   ea

    # grab covers and set them into their new location

    # generate config

    # set new config and covers
    get_games()
    ...


if __name__ == "__main__":
    main()
