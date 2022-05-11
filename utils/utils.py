from itertools import groupby
from typing import List


def clear_solution(scheduling_problem):
    for machine_index in zip(scheduling_problem.machines.index):
        scheduling_problem.machines.loc[machine_index, "assigned_jobs"].clear()
        scheduling_problem.machines.loc[machine_index, "processing_time"] = 0.0


def add_job_to_machine(scheduling_problem, machine_index, job_index):
    scheduling_problem.machines.loc[machine_index, "assigned_jobs"].append(job_index)
    scheduling_problem.machines.loc[machine_index, "processing_time"] = (
        max(
            scheduling_problem.machines.loc[machine_index, "processing_time"],
            scheduling_problem.jobs.loc[job_index, "release_date"],
        )
        + scheduling_problem.processing_times.loc[machine_index, job_index]
    )


def initialize_solution(scheduling_problem, grouped_vectorized_solution: List):
    clear_solution(scheduling_problem=scheduling_problem)
    scheduled_jobs = []
    for machine_index, jobs in zip(scheduling_problem.machines.index, grouped_vectorized_solution):
        for job_index in jobs:
            if job_index is not None:
                add_job_to_machine(
                    scheduling_problem=scheduling_problem, machine_index=machine_index, job_index=job_index
                )
                scheduled_jobs.append(job_index)
    return scheduling_problem, scheduled_jobs


def vectorize_solution(machines):
    solution_vector = []
    for jobs in machines["assigned_jobs"]:
        if len(jobs) > 0:
            for job in jobs:
                solution_vector.append(job)
        else:
            solution_vector.append(None)
        solution_vector.append("*")
    solution_vector.pop()
    return solution_vector


def get_grouped_solution(arr: List):
    return [list(group) for k, group in groupby(arr, lambda x: x == "*") if not k]
