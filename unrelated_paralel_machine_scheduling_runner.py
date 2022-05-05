from task_generator.unrelated_paralel_machine_generator import UnrelatedParallelMachineSchedulingGenerator


def main():
    problem = UnrelatedParallelMachineSchedulingGenerator()
    print(problem.machines)
    print()
    print(problem.jobs)
    print()
    print(problem.operation_processing_times)


if __name__ == "__main__":
    main()
