from dataclasses import dataclass, field
from data_type.constriction_coefficients import ConstrictionCoefficients

constriction_coefficients = ConstrictionCoefficients()


@dataclass
class PSOParams:
    iterations: int = 100
    swarm_size: int = 50
    R1_probability: float = 0.5
    R2_probability: float = 0.5

    def __post_init__(self):
        self.inertia_dampening = 1 - (self.inertia / self.iterations)
