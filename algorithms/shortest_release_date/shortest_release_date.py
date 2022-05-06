import numpy as np
import pandas as pd
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator


class ShortestReleaseDates:
    def __init__(self, problem: UnrelatedParallelMachineSchedulingGenerator):
        self.problem = problem
        self.unscheduled_jobs = self.problem.jobs.sort_values("release_date")
        self.machines_processing_times = np.zeros(self.problem.no_of_machines)

    def get_min_machine_index(self, job_index):
        sorted_machines = pd.concat(
            [self.problem.machines["processing_time"], self.problem.processing_times.loc[:, job_index]],
            axis=1,
        ).sort_values(["processing_time", job_index])

        return sorted_machines.iloc[0].name

    def assign_jobs(self):
        for job_index in self.unscheduled_jobs.index:
            min_machine_index = self.get_min_machine_index(job_index=job_index)
            self.problem.machines.loc[min_machine_index, "processing_time"] = (
                max(
                    self.problem.machines.loc[min_machine_index, "processing_time"],
                    self.problem.jobs.loc[job_index, "release_date"],
                )
                + self.problem.processing_times.loc[min_machine_index, job_index]
            )

            self.problem.machines.loc[min_machine_index, "assigned_jobs"].append(job_index)
