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
    plot_jobs(scheduling_solution=scheduling_problem)
    # SRD -------------------------------------
    SRD = ShortestReleaseDates()
    srd_solution = SRD.assign_jobs(scheduling_problem=scheduling_problem)
    srd_vector = vectorize_solution(machines=srd_solution.machines)
    srd_cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=srd_vector)

    print(f"SRD cost: {srd_cost}")
    gantt_plot(scheduling_solution=srd_solution, title="SRD", plot_label=False)

    # SA -------------------------------------
    # best_sa_params = None
    # for temperature in np.arange(start=0.5, stop=2.1, step=0.1):
    #     for cooling_rate in np.arange(start=0.49, stop=0.999, step=0.1):
    #         for iterations in np.arange(100, 5001, 100):
    #             start_time = time.time()
    #             simulated_annealing = SimulatedAnnealing(
    #                 temperature=temperature,
    #                 cooling_rate=cooling_rate,
    #                 max_iterations=iterations,
    #                 display_iteration=False,
    #             )
    #             sa_solution, sa_iterations = simulated_annealing.run(scheduling_problem=scheduling_problem)
    #             end_time = time.time()
    #             sa_params = SAParams(
    #                 processing_time=end_time - start_time,
    #                 temperature=temperature,
    #                 cooling_rate=cooling_rate,
    #                 best_solution=BestSolution(position=sa_solution.position, cost=sa_solution.cost),
    #                 iterations=sa_iterations,
    #             )
    #             if best_sa_params is None:
    #                 best_sa_params = sa_params
    #             if sa_params.best_solution.cost < best_sa_params.best_solution.cost:
    #                 best_sa_params = sa_params
    #             print(sa_params)
    #             if sa_iterations < iterations:
    #                 break
    # print()
    # print("BEST SA PARAMS ==================================================================================")
    # print(best_sa_params)
    # print("=================================================================================================")
    # print()
    # SA_solution, _ = initialize_solution(
    #     scheduling_problem=scheduling_problem,
    #     grouped_vectorized_solution=get_grouped_solution(simulated_annealing_solution.position),
    # )
    # print(f"SA cost: {simulated_annealing_solution.cost}")
    # gantt_plot(scheduling_solution=SA_solution, title="SA", plot_label=False)

    # plt.plot(simulated_annealing.best_cost_history)
    # plt.show()
    # plt.semilogy(simulated_annealing.best_cost_history)
    # plt.show()

    # PSO -----------------------------
    max_time = 90
    PSO_best_solution = None
    PSO_best_params = None
    for ls_iterations in range(0, 11):
        pso_probability = Probability(
            distribution="bernoulli",  # bernoulli or randint
            R1=0.9,
            R2=0.1,
            R1_dampening=0.0,
            R2_dampening=0.0,
        )
        pso_local_search = LocalSearch(
            end_with_local_search=True,
            iterations=ls_iterations,
        )
        pso_params = PSOParams(
            iterations=200,
            swarm_size=30,
            random_first_solution=False,
            initialize_method="shuffle",
            reverse_subtraction=False,
            multiplication_operator="regular",
            fill_velocity_randomly=False,
            R_probability=pso_probability,
            local_search=pso_local_search,
        )

        pso = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params)
        pso_solutions, pso_iterations = pso.run()
        if PSO_best_solution is None:
            PSO_best_solution = pso_solutions
        elif pso_solutions.cost < PSO_best_solution.cost:
            PSO_best_solution = pso_solutions
            PSO_best_params = pso_params
        pso_params.iterations = pso_iterations
        print(f"Params: {pso_params}, cost: {pso_solutions.cost}")
    print()
    print(f"SRD cost: {srd_cost}")
    print("BEST PSO PARAMS ==================================================================================")
    print(PSO_best_params)
    print("BEST PSO SOLUTION ==================================================================================")
    print(PSO_best_solution)
    print("=================================================================================================")
    print()
    # print()
    # print("BEST SA PARAMS ==================================================================================")
    # print(best_sa_params)
    # print("=================================================================================================")
    # print()

    # # PSO2 -----------------------------
    # pso_probability2 = Probability(
    #     distribution="randint",  # bernoulli or randint
    #     R1=0.9,
    #     R2=0.9,
    #     R1_dampening=0.0,
    #     R2_dampening=0.0,
    # )
    # pso_local_search2 = LocalSearch(
    #     end_with_local_search=True,
    #     iterations=10,
    # )
    # pso_params2 = PSOParams(
    #     iterations=500,
    #     swarm_size=30,
    #     random_first_solution=False,
    #     initialize_method="random",
    #     reverse_subtraction=True,
    #     multiplication_operator="regular",
    #     fill_velocity_randomly=True,
    #     R_probability=pso_probability2,
    #     local_search=pso_local_search2,
    # )
    # scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()

    # pso2 = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params2)
    # pso_solutions2 = pso2.run()

    # print(f"PSO2 cost: {pso_solutions2.cost}")
    # gantt_plot(scheduling_solution=pso_solutions, title="PSO", plot_label=False)
    # plt.plot(pso.best_costs)

    # plt.show()
    # plt.semilogy(pso.best_costs)
    # plt.show()

    # print()
    # print(f"SRD cost: {srd_cost}")
    # print(f"SA cost: {simulated_annealing_solution.cost}")
    # print(f"PSO cost: {pso_solutions.cost}")
    # print(f"PSO cost: {pso_solutions2.cost}")
    # print(f"PSO2 cost: {pso_solutions2.cost}")


if __name__ == "__main__":
    main()
