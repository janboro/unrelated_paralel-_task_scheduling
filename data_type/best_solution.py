from pydantic import BaseModel
from typing import List


class BestSolution(BaseModel):
    position: List
    cost: float
