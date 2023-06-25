from dataclasses import dataclass
from datetime import datetime


@dataclass
class Objava:
    naslov: str
    podnaslov: str
    vsebina: str
    slika: str
    objavljeno: datetime