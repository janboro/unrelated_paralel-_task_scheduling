import csv
import time
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.shortest_release_date import ShortestReleaseDates
from algorithms.particle_swarm_optimization import PSO
from data_type.PSO_params import PSOParams, Probability, LocalSearch
from utils.utils import vectorize_solution, get_solution_cost
from utils.plotter import gantt_plot, plot_jobs


def write_row_to_csv(row, file_name):
    with open(file_name, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)


def main():
    test_file_path = "runners/testing_results.csv"
    test_iterations = 1
    max_time = 8 * 60
    for no_of_machines, no_of_jobs in zip([15], [100]):
        row = [f"Machines: {no_of_machines}, Jobs: {no_of_jobs} ======================="]
        write_row_to_csv(row, test_file_path)

        scheduling_problem = UnrelatedParallelMachineSchedulingGenerator(
            no_of_machines=no_of_machines, no_of_jobs=no_of_jobs
        )
        # SRD -------------------------------------
        SRD = ShortestReleaseDates()
        start_time = time.time()
        srd_solution = SRD.assign_jobs(scheduling_problem=scheduling_problem)
        end_time = time.time()
        srd_vector = vectorize_solution(machines=srd_solution.machines)
        srd_cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=srd_vector)

        print(f"SRD cost: {srd_cost}")
        row = [f"Time: {end_time-start_time}", f"Cost: {srd_cost}"]
        write_row_to_csv(row=row, file_name=test_file_path)

        row = ["SA --------------------------"]
        write_row_to_csv(row, test_file_path)
        # SA -------------------------------------
        for _ in range(test_iterations):
            start_time = time.time()
            simulated_annealing = SimulatedAnnealing(
                temperature=1.0,
                cooling_rate=0.99,
                max_iterations=1000,
                max_time=60,
                display_iteration=False,
            )
            sa_solution, sa_iterations = simulated_annealing.run(scheduling_problem=scheduling_problem)
            end_time = time.time()
            sa_solution.cost
            row = [f"Time: {end_time-start_time}", f"Iterations: {sa_iterations}", f"Cost: {sa_solution.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)

        # Lit PSO -----------------------------
        row = ["Lit PSO --------------------------"]
        write_row_to_csv(row, test_file_path)
        for _ in range(test_iterations):
            start_time = time.time()
            pso_probability = Probability(
                distribution="bernoulli",  # bernoulli or randint
                R1=0.9,
                R2=0.1,
                R1_dampening=0.0,
                R2_dampening=0.0,
            )
            pso_local_search = LocalSearch(
                end_with_local_search=False,
                iterations=0,
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

            pso = PSO(
                scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False
            )
            pso_solutions, pso_iterations = pso.run()
            end_time = time.time()
            row = [f"Time: {end_time-start_time}", f"Iterations: {pso_iterations}", f"Cost: {pso_solutions.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)

        # Lit PSO + LS -----------------------------
        row = ["Lit PSO + LS --------------------------"]
        write_row_to_csv(row, test_file_path)
        for _ in range(test_iterations):
            start_time = time.time()
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

            pso = PSO(
                scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False
            )
            pso_solutions, pso_iterations = pso.run()
            end_time = time.time()
            row = [f"Time: {end_time-start_time}", f"Iterations: {pso_iterations}", f"Cost: {pso_solutions.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)

        # Aut PSO randint -----------------------------
        row = ["Aut PSO (Randint) --------------------------"]
        write_row_to_csv(row, test_file_path)
        for _ in range(test_iterations):
            start_time = time.time()
            pso_probability = Probability(
                distribution="randint",  # bernoulli or randint
                R1=0.0,
                R2=0.0,
                R1_dampening=0.0,
                R2_dampening=0.0,
            )
            pso_local_search = LocalSearch(
                end_with_local_search=False,
                iterations=0,
            )
            pso_params = PSOParams(
                iterations=3000,
                swarm_size=30,
                random_first_solution=True,
                initialize_method="random",
                reverse_subtraction=True,
                fill_velocity_randomly=True,
                R_probability=pso_probability,
                local_search=pso_local_search,
            )

            pso = PSO(
                scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False
            )
            pso_solutions, pso_iterations = pso.run()
            end_time = time.time()
            row = [f"Time: {end_time-start_time}", f"Iterations: {pso_iterations}", f"Cost: {pso_solutions.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)

        # Aut PSO bernouilli random first solution-----------------------------
        row = ["Aut PSO (bernouilli) random first --------------------------"]
        write_row_to_csv(row, test_file_path)
        for _ in range(test_iterations):
            start_time = time.time()
            pso_probability = Probability(
                distribution="bernoulli",  # bernoulli or randint
                R1=0.7,
                R2=0.8,
                R1_dampening=0.1,
                R2_dampening=0.3,
            )
            pso_local_search = LocalSearch(
                end_with_local_search=False,
                iterations=0,
            )
            pso_params = PSOParams(
                iterations=3000,
                swarm_size=30,
                random_first_solution=True,
                initialize_method="random",
                reverse_subtraction=True,
                fill_velocity_randomly=True,
                R_probability=pso_probability,
                local_search=pso_local_search,
            )

            pso = PSO(
                scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False
            )
            pso_solutions, pso_iterations = pso.run()
            end_time = time.time()
            row = [f"Time: {end_time-start_time}", f"Iterations: {pso_iterations}", f"Cost: {pso_solutions.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)

        # Aut PSO bernouilli SRD first solution  -----------------------------
        row = ["Aut PSO (bernouilli) shuffle first --------------------------"]
        write_row_to_csv(row, test_file_path)
        for _ in range(test_iterations):
            start_time = time.time()
            pso_probability = Probability(
                distribution="bernoulli",  # bernoulli or randint
                R1=0.7,
                R2=0.8,
                R1_dampening=0.1,
                R2_dampening=0.3,
            )
            pso_local_search = LocalSearch(
                end_with_local_search=False,
                iterations=0,
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

            pso = PSO(
                scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False
            )
            pso_solutions, pso_iterations = pso.run()
            end_time = time.time()
            row = [f"Time: {end_time-start_time}", f"Iterations: {pso_iterations}", f"Cost: {pso_solutions.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)

        # Aut PSO bernouilli SRD first solution + LS -----------------------------
        row = ["Aut PSO (bernouilli) shuffle first + LS --------------------------"]
        write_row_to_csv(row, test_file_path)
        for _ in range(test_iterations):
            start_time = time.time()
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

            pso = PSO(
                scheduling_problem=scheduling_problem, pso_params=pso_params, max_time=max_time, display_iteration=False
            )
            pso_solutions, pso_iterations = pso.run()
            end_time = time.time()
            row = [f"Time: {end_time-start_time}", f"Iterations: {pso_iterations}", f"Cost: {pso_solutions.cost}"]
            write_row_to_csv(row=row, file_name=test_file_path)


if __name__ == "__main__":
    main()
