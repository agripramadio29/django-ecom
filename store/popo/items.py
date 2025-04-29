from dataclasses import dataclass

@dataclass
class Item:
    image: str
    type: str
    name: str
    desc: str
    price: float