from typing import List
import numpy as np


class LocalSearch:
    def shuffle_solution(self, solution: List):
        a, b = np.random.randint(low=0, high=len(solution), size=2)
        solution[a], solution[b] = solution[b], solution[a]
        return solution
