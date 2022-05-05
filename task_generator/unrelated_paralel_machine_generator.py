import pandas as pd
import numpy as np
from config.config_handler import ParametersHandler


class UnrelatedParallelMachineSchedulingGenerator:
    machines_params = ParametersHandler().handler["machines"]
    jobs_params = ParametersHandler().handler["jobs"]

    def __init__(self):
        self.no_of_machines = np.random.randint(
            low=self.machines_params["amount"]["min"], high=self.machines_params["amount"]["max"]
        )
        self.no_of_jobs = np.random.randint(
            low=self.jobs_params["amount"]["min"], high=self.jobs_params["amount"]["max"]
        )
        self.machines = self.generate_machines()
        self.jobs = self.generate_jobs()
        self.operation_processing_times = self.generate_operations_processing_times()

    def generate_machines(self):

        machines = pd.DataFrame(
            data=[[[]] for _ in range(self.no_of_machines)], columns=["assigned_operations"]
        )  # TODO Do we need an operations queue?
        machines = machines.rename(index=lambda x: f"machine_{x}")
        return machines

    def generate_jobs(self):
        jobs_release_dates = np.random.randint(
            low=self.jobs_params["release_date"]["min"],
            high=self.jobs_params["release_date"]["max"],
            size=self.no_of_jobs,
        )

        jobs = pd.DataFrame(
            data=np.transpose([jobs_release_dates, jobs_release_dates]),
            columns=["release_date", "readiness_time"],
        )
        jobs = jobs.rename(index=lambda x: f"job_{x}")

        return jobs

    def generate_operations_processing_times(self):
        processing_times = np.random.randint(
            low=self.jobs_params["operation_processing_time"]["min"],
            high=self.jobs_params["operation_processing_time"]["max"],
            size=(self.no_of_machines, self.no_of_jobs),
        )

        processing_times = pd.DataFrame(processing_times)
        processing_times.name = "ProcessingTimes"
        processing_times = processing_times.rename(columns=lambda x: f"job_{x}", index=lambda x: f"machine_{x}")
        return processing_times
