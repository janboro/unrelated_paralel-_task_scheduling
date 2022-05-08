import numpy as np
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.operators import Operators
from algorithms.shortest_release_date import ShortestReleaseDates


def main():
    operators = Operators()

    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    SRD = ShortestReleaseDates()
    SRD.assign_jobs(scheduling_problem=scheduling_problem)

    print(scheduling_problem.machines)

    # vector_solution = operators.vectorize_solution(machines=problem.machines)
    # R = list(np.random.binomial(n=1, p=0.5, size=len(vector_solution)))
    # operators.multiply(A=R, B=vector_solution, problem=problem)

    # print(operators.vectorize_solution(machines=problem.machines))
    # print()

    A = [7, 6, 1, 4, "*", 3, 2, 5]
    B = [4, 7, 2, "*", 6, 3, 1, 5]
    print(operators.add(arr_A=A, arr_B=B))


if __name__ == "__main__":
    main()
