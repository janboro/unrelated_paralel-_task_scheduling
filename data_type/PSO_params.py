from typing import Optional
from pydantic import BaseModel


class Probability(BaseModel):
    distribution: str  # bernoulli or randint
    R1: Optional[float]
    final_R1: Optional[float]
    R2: Optional[float]
    final_R2: Optional[float]
    R1_dampening: Optional[float]
    R2_dampening: Optional[float]


class LocalSearch(BaseModel):
    end_with_local_search: bool
    iterations: int


class PSOParams(BaseModel):
    iterations: int
    swarm_size: int
    random_first_solution: bool
    initialize_method: str  # random or shuffle
    reverse_subtraction: bool  # regular or reversed
    multiplication_operator: str  # regular or local_search
    fill_velocity_randomly: bool
    R_probability: Probability
    local_search: LocalSearch
