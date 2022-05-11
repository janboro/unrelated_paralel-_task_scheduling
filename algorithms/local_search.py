from random import choice
from typing import List
import numpy as np
from utils.utils import get_grouped_solution


class LocalSearch:
    def shuffle_solution(self, solution: List):
        solution = list(filter(lambda x: x is not None, solution))
        a, b = np.random.randint(low=0, high=len(solution), size=2)
        solution[a], solution[b] = solution[b], solution[a]

        local_search_solution = []
        for i in range(len(solution)):
            if solution[i] == "*":
                if i == 0 or solution[i - 1] == "*":
                    local_search_solution.append(None)
                local_search_solution.append("*")
                if i == len(solution) - 1:
                    local_search_solution.append(None)
            else:
                local_search_solution.append(solution[i])

        return local_search_solution

    # def local_search(self, solution: List, scheduling_problem):
    #     max_processing_time_machine = max(scheduling_problem.machines.loc[:, "processing_time"])
    #     swap_machine = choice(scheduling_problem.machines.index)
    #     while swap_machine == max_processing_time_machine:
    #         swap_machine = choice(scheduling_problem.machines.index)

    #     grouped_solution = get_grouped_solution(arr=solution)

    #     solution = list(filter(lambda x: x is not None, solution))
    #     a, b = np.random.randint(low=0, high=len(solution), size=2)
