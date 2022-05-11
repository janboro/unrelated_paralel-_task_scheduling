import random
from utils.utils import clear_solution, add_job_to_machine


class RandomSolution:
    @staticmethod
    def generate_random_solution(scheduling_problem):
        clear_solution(scheduling_problem=scheduling_problem)

        unscheduled_jobs = scheduling_problem.jobs.sort_values("release_date")
        for job_index in unscheduled_jobs.index:
            machine_index = random.choice(scheduling_problem.machines.index)
            add_job_to_machine(scheduling_problem=scheduling_problem, machine_index=machine_index, job_index=job_index)
        return scheduling_problem

    @staticmethod
    def assign_randomly(scheduling_problem, scheduled_jobs=[]):
        for job_index in scheduling_problem.jobs.index:
            if job_index not in scheduled_jobs:
                machine_index = random.choice(scheduling_problem.machines.index)
                add_job_to_machine(
                    scheduling_problem=scheduling_problem, machine_index=machine_index, job_index=job_index
                )
        return scheduling_problem
