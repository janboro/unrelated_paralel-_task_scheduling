import numpy as np
from data_type.PSO_params import PSOParams
from data_type.particle import Particle
from data_type.best_solution import BestSolution
from algorithms.shortest_release_date import ShortestReleaseDates
from algorithms.random_solution import RandomSolution
from algorithms.operators import Operators
from algorithms.local_search import LocalSearch
from utils.utils import clear_solution, vectorize_solution, get_solution_cost


class PSO:
    def __init__(self, scheduling_problem, pso_params: PSOParams = PSOParams()):
        self.operators = Operators()
        self.SRD = ShortestReleaseDates()
        self.random_solution = RandomSolution()
        self.local_search = LocalSearch()
        self.scheduling_problem = scheduling_problem
        self.pso_params = pso_params
        self.global_best = None
        self.best_costs = []  # used to plot efficiency over time
        self.swarm = self.initialize_swarm()

    def get_lower_bounds(self, scheduling_problem):
        min_jobs_proscessing_times = scheduling_problem.processing_times.min()
        release_dates = scheduling_problem.jobs.loc[:, "release_date"]
        lower_bound_1 = max(min_jobs_proscessing_times + release_dates)
        lower_bound_2 = sum(min_jobs_proscessing_times) / len(scheduling_problem.machines)
        return max(lower_bound_1, lower_bound_2)

    def generate_first_particle(self, scheduling_problem, random=False):
        if random:
            clear_solution(scheduling_problem=scheduling_problem)
            initial_solution = self.random_solution.generate_random_solution(scheduling_problem=scheduling_problem)
        else:
            clear_solution(scheduling_problem=scheduling_problem)
            initial_solution = self.SRD.assign_jobs(scheduling_problem=scheduling_problem)
        initial_position = vectorize_solution(initial_solution.machines)
        cost = get_solution_cost(scheduling_problem=self.scheduling_problem, vectorized_solution=initial_position)
        particle = Particle(
            position=initial_position,
            velocity=initial_position,
            cost=cost,
            personal_best=BestSolution(position=initial_position, cost=cost),
        )

        self.global_best = particle.personal_best.copy()
        self.best_costs.append(self.global_best.cost)
        return particle

    def initialize_swarm(self):
        swarm = []
        for i in range(self.pso_params.swarm_size):
            if i == 0:
                swarm.append(self.generate_first_particle(scheduling_problem=self.scheduling_problem, random=True))
            else:
                # initial_position = self.local_search.shuffle_solution(solution=self.global_best.position.copy())
                initial_solution = self.random_solution.generate_random_solution(
                    scheduling_problem=self.scheduling_problem
                )
                initial_position = vectorize_solution(initial_solution.machines)

                cost = get_solution_cost(
                    scheduling_problem=self.scheduling_problem, vectorized_solution=initial_position
                )

                particle = Particle(
                    position=initial_position,
                    velocity=initial_position,
                    cost=cost,
                    personal_best=BestSolution(position=initial_position, cost=cost),
                )
                swarm.append(particle)
                self.update_global_best_solution(particle=particle)
        return swarm

    def get_new_velocity(self, particle: Particle):
        inertia_term = particle.velocity

        cognitive_component_substraction = self.operators.substract(
            arr_A=particle.personal_best.position, arr_B=particle.position, scheduling_problem=self.scheduling_problem
        )
        R1 = list(np.random.binomial(n=1, p=self.pso_params.R1_probability, size=len(cognitive_component_substraction)))
        cognitive_component = self.operators.multiply(
            arr_A=R1,
            arr_B=cognitive_component_substraction,
            scheduling_problem=self.scheduling_problem,
        )

        social_component_substraction = self.operators.substract(
            arr_A=self.global_best.position, arr_B=particle.position, scheduling_problem=self.scheduling_problem
        )
        R2 = list(np.random.binomial(n=1, p=self.pso_params.R2_probability, size=len(social_component_substraction)))
        social_component = self.operators.multiply(
            arr_A=R2,
            arr_B=social_component_substraction,
            scheduling_problem=self.scheduling_problem,
        )

        velocity = self.operators.add(
            arr_A=inertia_term, arr_B=self.operators.add(arr_A=cognitive_component, arr_B=social_component)
        )
        return velocity

    def update_global_best_solution(self, particle: Particle):
        if particle.personal_best.cost < self.global_best.cost:
            self.global_best = particle.personal_best
            self.best_costs.append(self.global_best.cost)

    def update_particle_best_solution(self, particle: Particle):
        if particle.cost < particle.personal_best.cost:
            particle.personal_best.position = particle.position
            particle.personal_best.cost = particle.cost
            self.update_global_best_solution(particle=particle)

    def run(self):
        for i in range(self.pso_params.iterations):
            print(f"Iteration: {i}")
            print(f"Best solution cost: {self.global_best.cost}")
            for particle in self.swarm:
                velocity = self.get_new_velocity(particle=particle)

                particle.velocity = velocity
                particle.position = self.operators.add(arr_A=particle.position, arr_B=particle.velocity)
                particle.cost = get_solution_cost(
                    scheduling_problem=self.scheduling_problem, vectorized_solution=particle.position
                )

                self.update_particle_best_solution(particle=particle)

            self.best_costs.append(self.global_best.cost)

        return self.global_best
