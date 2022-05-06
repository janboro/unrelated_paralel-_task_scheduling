from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.shortest_release_date.shortest_release_date import ShortestReleaseDates


def main():
    problem = UnrelatedParallelMachineSchedulingGenerator()
    SRD = ShortestReleaseDates(problem=problem)
    SRD.assign_jobs()

    print(problem.jobs)
    print(problem.processing_times)
    print(problem.machines)


if __name__ == "__main__":
    main()
