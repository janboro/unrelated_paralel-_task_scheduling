import numpy as np
from data_type.simulated_annealing_particle import SAParticle
from algorithms.random_solution import RandomSolution
from algorithms.local_search import LocalSearch
from utils.utils import vectorize_solution, get_solution_cost


class SimulatedAnnealing:
    def __init__(self):
        self.random_solution = RandomSolution()
        self.local_search = LocalSearch()
        self.temperature = 1
        self.cooling_rate = 0.99
        self.max_iterations = 30
        self.best_solution = None
        self.bets_cost_history = []

    def get_initial_solution(self, scheduling_problem):
        initial_solution = self.random_solution.generate_random_solution(scheduling_problem=scheduling_problem)
        initial_cost = max(initial_solution.machines.loc[:, "processing_time"])
        initial_position = vectorize_solution(machines=initial_solution.machines)
        particle = SAParticle(position=initial_position, cost=initial_cost)
        return particle

    def get_neighbour(self, particle, scheduling_problem):
        neighbouring_solution = self.local_search.shuffle_solution(solution=particle.position)
        cost = get_solution_cost(scheduling_problem=scheduling_problem, vectorized_solution=neighbouring_solution)
        neighbour = SAParticle(position=neighbouring_solution, cost=cost)
        return neighbour

    def run(self, scheduling_problem):
        A = self.get_initial_solution(scheduling_problem=scheduling_problem)

        self.best_solution = A
        self.bets_cost_history.append(A.cost)

        for _ in range(self.max_iterations):
            neighbour = self.get_neighbour(particle=A, scheduling_problem=scheduling_problem)

            delta = neighbour.cost - A.cost
            if delta < 0:
                A = neighbour
                self.best_solution = A
                self.bets_cost_history.append(A.cost)
            else:
                p = np.random.rand()
                if p < np.exp(-delta / self.temperature):
                    A = neighbour
                    self.bets_cost_history.append(A.cost)
            self.temperature *= self.cooling_rate

        return self.best_solution
