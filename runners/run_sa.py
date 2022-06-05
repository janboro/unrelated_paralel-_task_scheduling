import matplotlib.pyplot as plt
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.simulated_annealing import SimulatedAnnealing
from utils.utils import get_grouped_solution, initialize_solution
from utils.plotter import gantt_plot, plot_jobs


def main():
    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()
    plot_jobs(scheduling_solution=scheduling_problem)

    simulated_annealing = SimulatedAnnealing(
        temperature=1,
        cooling_rate=0.99,
        max_iterations=500,
        display_iteration=False,
    )
    sa_solution, _ = simulated_annealing.run(scheduling_problem=scheduling_problem)

    SA_solution, _ = initialize_solution(
        scheduling_problem=scheduling_problem,
        grouped_vectorized_solution=get_grouped_solution(sa_solution.position),
    )
    print(f"SA cost: {sa_solution.cost}")
    gantt_plot(scheduling_solution=SA_solution, title="SA", plot_label=False)

    plt.plot(simulated_annealing.best_cost_history, color="tab:blue")
    plt.show()
    plt.semilogy(simulated_annealing.best_cost_history, color="tab:blue")
    plt.show()


if __name__ == "__main__":
    main()
