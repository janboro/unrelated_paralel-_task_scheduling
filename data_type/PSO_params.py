from dataclasses import dataclass


@dataclass
class PSOParams:
    iterations: int = 100
    swarm_size: int = 50
    R1_probability: float = 0.5
    R2_probability: float = 0.5
