from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.particle_swarm_optimization.operators import Operators
from algorithms.shortest_release_date.shortest_release_date import ShortestReleaseDates


def main():
    operators = Operators()

    problem = UnrelatedParallelMachineSchedulingGenerator()
    SRD = ShortestReleaseDates(problem=problem)
    SRD.assign_jobs()

    A = [3, 4, 1, 2, "*", 5, 7, 6]
    print(operators.multiply(A=A))


if __name__ == "__main__":
    main()
