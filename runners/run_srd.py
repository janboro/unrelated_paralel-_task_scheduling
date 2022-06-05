from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.shortest_release_date import ShortestReleaseDates
from utils.utils import vectorize_solution, get_solution_cost
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


if __name__ == "__main__":
    main()
