import numpy as np
from data_type.PSO_params import PSOParams
from data_type.problem import Problem
from data_type.particle import Particle
from data_type.problem import Problem
from data_type.best_solution import BestSolution
from algorithms.shortest_release_date import ShortestReleaseDates
from algorithms.operators import Operators
from algorithms.local_search import LocalSearch


class PSO:
    def __init__(self, scheduling_problem, problem: Problem, pso_params: PSOParams = PSOParams()):
        self.operators = Operators()
        self.SRD = ShortestReleaseDates()
        self.local_search = LocalSearch()
        self.scheduling_problem = scheduling_problem
        self.problem = problem
        self.pso_params = pso_params
        self.global_best = BestSolution(cost=float("inf"))
        self.swarm = self.initialize_swarm()
        self.best_costs = []  # used to plot efficiency over time

    def get_lower_bounds(self, scheduling_problem):
        min_jobs_proscessing_times = scheduling_problem.processing_times.min()
        release_dates = scheduling_problem.jobs.loc[:, "release_date"]
        lower_bound_1 = max(min_jobs_proscessing_times + release_dates)
        lower_bound_2 = sum(min_jobs_proscessing_times) / len(scheduling_problem.machines)
        return max(lower_bound_1, lower_bound_2)

    def get_solution_cost(self, vectorized_solution):
        grouped_vectorized_solution = self.operators.get_grouped_solution(arr=vectorized_solution)
        solution, _ = self.SRD.initialize_solution(
            scheduling_problem=self.scheduling_problem.copy(),
            grouped_vectorized_solution=grouped_vectorized_solution,
        )
        return max(solution.machines.loc[:, "processing_time"])

    def generate_first_particle(self, scheduling_problem):
        initial_solution = self.SRD.assign_jobs(scheduling_problem=scheduling_problem)
        initial_position = self.operators.vectorize_solution(initial_solution)
        cost = self.get_solution_cost(vectorized_solution=initial_position)
        particle = Particle(
            position=initial_position,
            velocity=initial_position,
            cost=cost,
            personal_best=BestSolution(position=initial_position, cost=cost),
        )

        self.global_best = particle.personal_best
        return particle

    def initialize_swarm(self):
        swarm = []
        for i in range(self.pso_params.swarm_size):
            if i == 1:
                swarm.append(self.generate_first_particle(scheduling_problem=self.scheduling_problem.copy()))
            else:
                initial_position = self.local_search.shuffle_solution(solution=self.global_best.position)
                cost = self.get_solution_cost(vectorized_solution=initial_position)

                particle = Particle(
                    position=initial_position,
                    velocity=initial_position,
                    cost=cost,
                    personal_best=BestSolution(position=initial_position, cost=cost),
                )
                swarm.append(particle)
                if particle.personal_best.cost < self.global_best.cost:
                    self.global_best = particle.personal_best
        return swarm

    def get_new_velocity(self, particle: Particle):
        inertia_term = particle.velocity
        R1 = list(np.random.binomial(n=1, p=self.pso_params.R1_probability, size=len(particle.position)))
        cognitive_component = self.operators.multiply(
            arr_A=R1,
            arr_B=self.operators.substract(arr_A=particle.personal_best.position, arr_B=particle.position),
            scheduling_problem=self.scheduling_problem.copy(),
        )

        R2 = list(np.random.binomial(n=1, p=self.pso_params.R2_probability, size=len(particle.position)))
        social_component = self.operators.multiply(
            arr_A=R2,
            arr_B=self.operators.substract(arr_A=self.global_best.position, arr_B=particle.position),
            scheduling_problem=self.scheduling_problem.copy(),
        )

        velocity = self.operators.add(
            arr_A=inertia_term, arr_B=self.operators.add(arr_A=cognitive_component, arr_B=social_component)
        )
        return velocity

    def update_global_best_solution(self, particle: Particle):
        if particle.personal_best.cost < self.global_best.cost:
            self.global_best = particle.personal_best

    def update_particle_best_solution(self, particle: Particle):
        if particle.cost < particle.personal_best.cost:
            particle.personal_best.position = particle.position
            particle.personal_best.cost = particle.cost
            self.update_global_best_solution(particle=particle)

    def run(self):
        for i in range(self.pso_params.iterations):
            print(f"Iteration: {i}")
            for particle in self.swarm:
                velocity = self.get_new_velocity(particle=particle)

                particle.velocity = velocity
                particle.position = self.operators.add(arr_A=particle.position, arr_B=particle.velocity)
                particle.cost = self.get_solution_cost(vectorized_solution=particle.position)

                self.update_particle_best_solution(particle=particle)

            self.best_costs.append(self.global_best.cost)

        return self.global_best
