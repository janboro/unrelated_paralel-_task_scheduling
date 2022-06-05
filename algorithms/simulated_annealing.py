import time
import numpy as np
from data_type.simulated_annealing_particle import SAParticle
from algorithms.random_solution import RandomSolution
from algorithms.local_search import LocalSearch
from utils.utils import vectorize_solution, get_solution_cost


class SimulatedAnnealing:
    def __init__(
        self,
        temperature,
        cooling_rate,
        max_iterations,
        display_iteration=False,
        max_time: float = 90.0,
        min_temperature: float = 0.000001,
    ):
        self.random_solution = RandomSolution()
        self.local_search = LocalSearch()
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.max_iterations = max_iterations
        self.best_solution = None
        self.best_cost_history = []
        self.display_iteration = display_iteration
        self.max_time = max_time
        self.min_temperature = min_temperature

    def get_initial_solution(self, scheduling_problem) -> SAParticle:
        initial_solution = self.random_solution.generate_random_solution(scheduling_problem=scheduling_problem)
        initial_cost = max(initial_solution.machines.loc[:, "processing_time"])
        initial_position = vectorize_solution(machines=initial_solution.machines)
        particle = SAParticle(position=initial_position, cost=initial_cost)
        return particle

    def get_neighbour(self, particle, scheduling_problem) -> SAParticle:
        neighbouring_solution = self.local_search.swap(solution=particle.position)
        cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=neighbouring_solution)
        neighbour = SAParticle(position=neighbouring_solution, cost=cost)
        return neighbour

    def run(self, scheduling_problem):
        start_time = time.time()
        A = self.get_initial_solution(scheduling_problem=scheduling_problem)

        self.best_solution = A
        self.best_cost_history.append(A.cost)
        iterations = 0
        for i in range(self.max_iterations):
            iterations = i + 1
            if time.time() - start_time > self.max_time:
                print(f"Reached limit time in iteration {i}")
                break
            if self.temperature < self.min_temperature:
                self.cooling_rate = 1.0
            if self.display_iteration:
                print(f"NA iteration: {i}")
            neighbour = self.get_neighbour(particle=A, scheduling_problem=scheduling_problem)

            delta = neighbour.cost - A.cost
            if delta < 0:
                A = neighbour
                self.best_solution = A
                self.best_cost_history.append(A.cost)
            else:
                p = np.random.rand()
                if p < np.exp(-delta / self.temperature):
                    A = neighbour
                    self.best_cost_history.append(A.cost)
            self.temperature *= self.cooling_rate

        return self.best_solution, iterations
