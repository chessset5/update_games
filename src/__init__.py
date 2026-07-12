from pathlib import Path

WORKSPACE: Path = Path(__file__).parent.parent
DATA_FOLDER: Path = WORKSPACE / "data"
CONFIG_FOLDER: Path = WORKSPACE / "config"

# Services
STEAM = "steam"
UBISOFT = "uplay"
EPIC = "epic"
GOG = "gog"
