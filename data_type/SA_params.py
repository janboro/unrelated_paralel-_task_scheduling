from typing import Optional
from pydantic import BaseModel
from data_type.best_solution import BestSolution


class SAParams(BaseModel):
    processing_time: float
    temperature: float
    cooling_rate: float
    best_solution: BestSolution
    iterations: Optional[int]
