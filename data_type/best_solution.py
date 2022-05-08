import numpy as np
from pydantic import BaseModel
from typing import List


class BestSolution(BaseModel):
    position: List
    cost: float

    class Config:
        arbitrary_types_allowed = True
