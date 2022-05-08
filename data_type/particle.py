from typing import List
from pydantic import BaseModel
from data_type.best_solution import BestSolution


class Particle(BaseModel):
    position: List
    velocity: List
    cost: float
    personal_best: BestSolution

    class Config:
        arbitrary_types_allowed = True
