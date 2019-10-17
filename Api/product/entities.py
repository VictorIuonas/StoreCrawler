from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: int
    title: str
    price: int
    currency: str
    description: Optional[str]
