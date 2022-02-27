from os.path import abspath
from pathlib import Path
from json import loads

assets_path = Path(abspath(__file__)).parent / "assets"

with open(assets_path / "enums.json", "rb") as F:
    enums = loads(F.read())