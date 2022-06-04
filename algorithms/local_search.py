from random import choice
from typing import List
import numpy as np
from utils.utils import get_grouped_solution, vectorize_grouped_solution, get_solution_cost


class LocalSearch:
    def cleanup_solution(self, solution: List):
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

    def swap(self, solution: List):
        solution = list(filter(lambda x: x is not None, solution))
        a, b = np.random.randint(low=0, high=len(solution), size=2)
        solution[a], solution[b] = solution[b], solution[a]

        return self.cleanup_solution(solution=solution)

    def insert(self, solution: List):
        solution = list(filter(lambda x: x is not None, solution))
        a, b = np.random.randint(low=0, high=len(solution), size=2)
        job_to_insert = solution.pop(a)
        solution.insert(b, job_to_insert)

        return self.cleanup_solution(solution=solution)

    def shorten_Cmax(self, solution: List, scheduling_problem):
        max_processing_time_machine = scheduling_problem.machines.loc[:, "processing_time"].idxmax()
        swap_machine = choice(scheduling_problem.machines.index)
        while swap_machine == max_processing_time_machine:
            swap_machine = choice(scheduling_problem.machines.index)

        grouped_solution = get_grouped_solution(arr=solution)

        solution = list(filter(lambda x: x is not None, solution))
        a = np.random.randint(low=0, high=len(scheduling_problem.machines.loc[swap_machine, ["assigned_jobs"]]))
        job_to_insert = grouped_solution[max_processing_time_machine].pop(a)
        grouped_solution[swap_machine].append(job_to_insert)
        return vectorize_grouped_solution(grouped_solution=grouped_solution)

    def local_search_procedure(self, solution: List, scheduling_problem, local_search_iterations: int, global_best):
        best_solution = global_best.copy()
        for _ in range(local_search_iterations):
            cmax_improved = True
            global_improved = True
            while global_improved:
                while cmax_improved:
                    solution = self.shorten_Cmax(solution=solution, scheduling_problem=scheduling_problem)
                    cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=solution)
                    if cost >= best_solution.cost:
                        cmax_improved = False
                    else:
                        best_solution.position = solution
                        best_solution.cost = cost

                global_best_position = best_solution.position.copy()
                self.swap(solution=global_best_position)
                cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=solution)
                if cost >= best_solution.cost:
                    global_improved = False
                else:
                    best_solution.position = solution
                    best_solution.cost = cost
        return best_solution.position, best_solution.cost
