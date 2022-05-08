import numpy as np
import pandas as pd
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator


class ShortestReleaseDates:
    def initialize_solution(self, scheduling_problem, grouped_vectorized_solution):
        scheduled_jobs = []
        for machine_index, jobs in zip(scheduling_problem.machines.index, grouped_vectorized_solution):
            scheduling_problem.machines.loc[machine_index, "assigned_jobs"].clear()
            scheduling_problem.machines.loc[machine_index, "processing_time"] = 0.0
            for job_index in jobs:
                if job_index == "*":
                    break
                elif job_index is not None:
                    self.add_job_to_machine(
                        scheduling_problem=scheduling_problem, machine_index=machine_index, job_index=job_index
                    )
                    scheduled_jobs.append(job_index)
        return scheduled_jobs

    def add_job_to_machine(self, scheduling_problem, machine_index, job_index):
        scheduling_problem.machines.loc[machine_index, "assigned_jobs"].append(job_index)
        scheduling_problem.machines.loc[machine_index, "processing_time"] = (
            max(
                scheduling_problem.machines.loc[machine_index, "processing_time"],
                scheduling_problem.jobs.loc[job_index, "release_date"],
            )
            + scheduling_problem.processing_times.loc[machine_index, job_index]
        )

    def get_min_machine_index(self, scheduling_problem, job_index):
        sorted_machines = pd.concat(
            [scheduling_problem.machines["processing_time"], scheduling_problem.processing_times.loc[:, job_index]],
            axis=1,
        ).sort_values(["processing_time", job_index])

        return sorted_machines.iloc[0].name

    def assign_jobs(self, scheduling_problem, scheduled_jobs=[]):
        unscheduled_jobs = scheduling_problem.jobs.sort_values("release_date")
        for job_index in unscheduled_jobs.index:
            if job_index not in scheduled_jobs:
                min_machine_index = self.get_min_machine_index(
                    scheduling_problem=scheduling_problem, job_index=job_index
                )
                self.add_job_to_machine(
                    scheduling_problem=scheduling_problem, machine_index=min_machine_index, job_index=job_index
                )
