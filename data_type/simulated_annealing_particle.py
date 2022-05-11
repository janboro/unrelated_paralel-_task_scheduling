from dataclasses import dataclass
from numpy.typing import ArrayLike


@dataclass
class SAParticle:
    position: ArrayLike
    cost: float
