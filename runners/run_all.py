import time
import numpy as np
import matplotlib.pyplot as plt
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.shortest_release_date import ShortestReleaseDates
from algorithms.particle_swarm_optimization import PSO
from data_type.PSO_params import PSOParams, Probability, LocalSearch
from data_type.SA_params import SAParams
from data_type.best_solution import BestSolution
from utils.utils import vectorize_solution, get_solution_cost, get_grouped_solution, initialize_solution
from utils.plotter import gantt_plot, plot_jobs


def main():
    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    print(scheduling_problem.jobs)
    print(scheduling_problem.processing_times)
    print()
    plot_jobs(scheduling_solution=scheduling_problem)
    # SRD -------------------------------------
    SRD = ShortestReleaseDates()
    srd_solution = SRD.assign_jobs(scheduling_problem=scheduling_problem)
    srd_vector = vectorize_solution(machines=srd_solution.machines)
    srd_cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=srd_vector)

    print(f"SRD cost: {srd_cost}")
    print(f"SRD solution: {srd_vector}")
    gantt_plot(scheduling_solution=srd_solution, title="SRD", plot_label=False)

    # SA -------------------------------------
    best_sa_params = None
    simulated_annealing = SimulatedAnnealing(
        temperature=1.0,
        cooling_rate=0.99,
        max_iterations=5000,
        display_iteration=False,
    )
    sa_solution, _ = simulated_annealing.run(scheduling_problem=scheduling_problem)

    SA_solution, _ = initialize_solution(
        scheduling_problem=scheduling_problem,
        grouped_vectorized_solution=get_grouped_solution(sa_solution.position),
    )
    print(f"SA cost: {sa_solution.cost}")
    print(f"SA solution: {sa_solution.position}")
    gantt_plot(scheduling_solution=SA_solution, title="SA", plot_label=False)

    plt.plot(simulated_annealing.best_cost_history, color="tab:blue")
    plt.show()
    plt.semilogy(simulated_annealing.best_cost_history, color="tab:blue")
    plt.show()

    # PSO 1 -----------------------------
    max_time = 180
    pso_probability = Probability(
        distribution="bernoulli",  # bernoulli or randint
        R1=0.9,
        R2=0.1,
        R1_dampening=0.0,
        R2_dampening=0.0,
    )
    pso_local_search = LocalSearch(
        end_with_local_search=True,
        iterations=10,
    )
    pso_params = PSOParams(
        iterations=3000,
        swarm_size=30,
        random_first_solution=False,
        initialize_method="shuffle",
        reverse_subtraction=False,
        fill_velocity_randomly=False,
        R_probability=pso_probability,
        local_search=pso_local_search,
    )

    pso = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False)
    pso_solutions, _ = pso.run()

    print(f"PSO1 cost: {pso_solutions.cost}")
    print(f"PSO1 solution: {pso_solutions}")
    print()
    PSO_solution, _ = initialize_solution(
        scheduling_problem=scheduling_problem,
        grouped_vectorized_solution=get_grouped_solution(pso_solutions.position),
    )
    gantt_plot(scheduling_solution=PSO_solution, title="PSO_LIT", plot_label=False)

    plt.plot(pso.best_costs, color="tab:blue")
    plt.show()
    plt.semilogy(pso.best_costs, color="tab:blue")
    plt.show()

    # PSO 2 -----------------------------
    max_time = 180
    pso_probability = Probability(
        distribution="bernoulli",  # bernoulli or randint
        R1=0.7,
        R2=0.8,
        R1_dampening=0.1,
        R2_dampening=0.3,
    )
    pso_local_search = LocalSearch(
        end_with_local_search=True,
        iterations=10,
    )
    pso_params = PSOParams(
        iterations=3000,
        swarm_size=30,
        random_first_solution=False,
        initialize_method="shuffle",
        reverse_subtraction=True,
        fill_velocity_randomly=True,
        R_probability=pso_probability,
        local_search=pso_local_search,
    )

    pso = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False)
    pso_solutions, _ = pso.run()

    print(f"PSO2 cost: {pso_solutions.cost}")
    print(f"PSO2 solution: {pso_solutions}")
    print()
    PSO_solution, _ = initialize_solution(
        scheduling_problem=scheduling_problem,
        grouped_vectorized_solution=get_grouped_solution(pso_solutions.position),
    )
    gantt_plot(scheduling_solution=PSO_solution, title="PSO_B_SRD_LS", plot_label=False)

    plt.plot(pso.best_costs, color="tab:blue")
    plt.show()
    plt.semilogy(pso.best_costs, color="tab:blue")
    plt.show()


if __name__ == "__main__":
    main()
