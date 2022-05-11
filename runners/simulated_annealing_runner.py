import matplotlib.pyplot as plt
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.shortest_release_date import ShortestReleaseDates
from utils.utils import vectorize_solution, get_solution_cost


def main():
    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    SRD = ShortestReleaseDates()
    srd_solution = SRD.assign_jobs(scheduling_problem=scheduling_problem)
    srd_vector = vectorize_solution(machines=srd_solution.machines)
    srd_cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=srd_vector)
    print(f"SRD cost: {srd_cost}")

    simulated_annealing = SimulatedAnnealing()
    best_solution = simulated_annealing.run(scheduling_problem=scheduling_problem)

    print(f"SA cost: {best_solution.cost}")

    plt.plot(simulated_annealing.bets_cost_history)
    plt.show()
    plt.semilogy(simulated_annealing.bets_cost_history)
    plt.show()


if __name__ == "__main__":
    main()