from typing import List, Optional
from pydantic import BaseModel


class AlgorithmTestResults(BaseModel):
    computing_times: List[float]
    iterations: List[int]
    costs: List[float]
    best_cost: Optional[float]
    worst_cost: Optional[float]
    mean: Optional[float]
    std: Optional[float]
