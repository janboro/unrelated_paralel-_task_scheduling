import numpy as np
import pandas as pd
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator


class ShortestReleaseDates:
    def __init__(self, problem: UnrelatedParallelMachineSchedulingGenerator, scheduled_jobs=[]):
        self.problem = problem
        self.scheduled_jobs = scheduled_jobs
        self.unscheduled_jobs = self.problem.jobs.sort_values("release_date")

    def initialize_solution(self, grouped_vectorized_solution):
        scheduled_jobs = []
        for machine_index, jobs in zip(self.problem.machines.index, grouped_vectorized_solution):
            self.problem.machines.loc[machine_index, "assigned_jobs"].clear()
            self.problem.machines.loc[machine_index, "processing_time"] = 0.0
            for job_index in jobs:
                if job_index == "*":
                    break
                elif job_index is not None:
                    self.add_job_to_machine(machine_index=machine_index, job_index=job_index)
                    scheduled_jobs.append(job_index)
        return scheduled_jobs

    def add_job_to_machine(self, machine_index, job_index):
        self.problem.machines.loc[machine_index, "assigned_jobs"].append(job_index)
        self.problem.machines.loc[machine_index, "processing_time"] = (
            max(
                self.problem.machines.loc[machine_index, "processing_time"],
                self.problem.jobs.loc[job_index, "release_date"],
            )
            + self.problem.processing_times.loc[machine_index, job_index]
        )

    def get_min_machine_index(self, job_index):
        sorted_machines = pd.concat(
            [self.problem.machines["processing_time"], self.problem.processing_times.loc[:, job_index]],
            axis=1,
        ).sort_values(["processing_time", job_index])

        return sorted_machines.iloc[0].name

    def assign_jobs(self):
        for job_index in self.unscheduled_jobs.index:
            if job_index not in self.scheduled_jobs:
                min_machine_index = self.get_min_machine_index(job_index=job_index)
                self.add_job_to_machine(machine_index=min_machine_index, job_index=job_index)
