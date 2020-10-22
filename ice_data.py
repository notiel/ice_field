from dataclasses import *
from typing import List


@dataclass
class IceField:
    height: int = 3
    width: int = 3
    knowledge: int = 0
    field: List[List[int]] = field(default_factory=list)
