import pandas as pd
from utils.utils import add_job_to_machine


class ShortestReleaseDates:
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
                add_job_to_machine(
                    scheduling_problem=scheduling_problem, machine_index=min_machine_index, job_index=job_index
                )
        return scheduling_problem
