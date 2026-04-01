from dataclasses import dataclass
from typing import List

@dataclass
class Place:
    region: str
    city: str
    street: str
    coord: str

class Article:
    def __init__(self, url: str, places: List[Place]):
        self.url = url
        self.places = places.copy()
