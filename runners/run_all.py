import matplotlib.pyplot as plt
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.shortest_release_date import ShortestReleaseDates
from algorithms.particle_swarm_optimization import PSO
from data_type.PSO_params import PSOParams
from utils.utils import vectorize_solution, get_solution_cost, get_grouped_solution, initialize_solution
from utils.plotter import gantt_plot, plot_jobs


def main():
    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    plot_jobs(scheduling_solution=scheduling_problem)
    # SRD -------------------------------------
    SRD = ShortestReleaseDates()
    srd_solution = SRD.assign_jobs(scheduling_problem=scheduling_problem)
    srd_vector = vectorize_solution(machines=srd_solution.machines)
    srd_cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=srd_vector)

    print(f"SRD cost: {srd_cost}")
    gantt_plot(scheduling_solution=srd_solution, title="SRD", plot_label=False)

    # SA -------------------------------------
    simulated_annealing = SimulatedAnnealing(
        temperature=1, cooling_rate=0.99, max_iterations=5000, display_iteration=True
    )
    simulated_annealing_solution = simulated_annealing.run(scheduling_problem=scheduling_problem)
    SA_solution, _ = initialize_solution(
        scheduling_problem=scheduling_problem,
        grouped_vectorized_solution=get_grouped_solution(simulated_annealing_solution.position),
    )
    print(f"SA cost: {simulated_annealing_solution.cost}")
    gantt_plot(scheduling_solution=SA_solution, title="SA", plot_label=False)

    plt.plot(simulated_annealing.bets_cost_history)
    plt.show()
    plt.semilogy(simulated_annealing.bets_cost_history)
    plt.show()

    # PSO -----------------------------
    # pso_params = PSOParams(iterations=5000, swarm_size=50, R1_probability=0.5, R2_probability=0.5)
    # scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()

    # pso = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params)
    # pso_solutions = pso.run()

    # # PSO2 -----------------------------
    # pso_params2 = PSOParams(iterations=5000, swarm_size=50, R1_probability=0.9, R2_probability=0.9)
    # scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()

    # pso2 = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params2)
    # pso_solutions2 = pso2.run()

    # print(f"PSO cost: {pso_solutions.cost}")
    # gantt_plot(scheduling_solution=pso_solutions, title="PSO", plot_label=False)
    # plt.plot(pso.best_costs)

    # plt.show()
    # plt.semilogy(pso.best_costs)
    # plt.show()

    print()
    print(f"SRD cost: {srd_cost}")
    print(f"SA cost: {simulated_annealing_solution.cost}")
    # print(f"PSO cost: {pso_solutions.cost}")
    # print(f"PSO2 cost: {pso_solutions2.cost}")


if __name__ == "__main__":
    main()
