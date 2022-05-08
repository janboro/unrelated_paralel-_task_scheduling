import numpy as np
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.operators import Operators
from algorithms.shortest_release_date import ShortestReleaseDates
from algorithms.local_search import LocalSearch


def main():
    operators = Operators()
    local_search = LocalSearch()

    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    SRD = ShortestReleaseDates()
    SRD.assign_jobs(scheduling_problem=scheduling_problem)

    print(scheduling_problem.machines)

    # vector_solution = operators.vectorize_solution(machines=problem.machines)
    # R = list(np.random.binomial(n=1, p=0.5, size=len(vector_solution)))
    # operators.multiply(A=R, B=vector_solution, problem=problem)

    # print()

    A = [7, 6, 1, 4, "*", 3, 2, 5]
    B = [4, 7, 2, "*", 6, 3, 1, 5]
    # print(local_search.shuffle_solution(solution=A))
    # print(operators.add(arr_A=A, arr_B=B))


if __name__ == "__main__":
    main()
