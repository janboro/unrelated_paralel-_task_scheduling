import matplotlib.pyplot as plt
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.particle_swarm_optimization import PSO
from data_type.PSO_params import PSOParams, Probability, LocalSearch
from utils.utils import get_grouped_solution, initialize_solution
from utils.plotter import gantt_plot, plot_jobs


def main():
    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    plot_jobs(scheduling_solution=scheduling_problem)
    # PSO -----------------------------
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
        iterations=500,
        swarm_size=25,
        random_first_solution=True,
        initialize_method="random",  # shuffle or random
        reverse_subtraction=True,
        fill_velocity_randomly=False,
        R_probability=pso_probability,
        local_search=pso_local_search,
    )

    pso = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params)
    pso_solutions, _ = pso.run()

    PSO_solution, _ = initialize_solution(
        scheduling_problem=scheduling_problem,
        grouped_vectorized_solution=get_grouped_solution(pso_solutions.position),
    )
    print(f"PSO cost: {pso_solutions.cost}")
    gantt_plot(scheduling_solution=PSO_solution, title="PSO", plot_label=False)

    plt.plot(pso.best_costs, color="tab:blue")
    plt.show()
    plt.semilogy(pso.best_costs, color="tab:blue")
    plt.show()


if __name__ == "__main__":
    main()
