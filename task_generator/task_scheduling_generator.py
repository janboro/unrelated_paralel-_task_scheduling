import pandas as pd
import numpy as np
from config.config_handler import ParametersHandler


class UnrelatedParallelMachineSchedulingGenerator:
    machines_params = ParametersHandler().handler["machines"]
    jobs_params = ParametersHandler().handler["jobs"]

    def __init__(self):
        self.no_of_machines = self.machines_params["amount"]
        self.no_of_jobs = self.jobs_params["amount"]
        self.machines = self.generate_machines()
        self.jobs = self.generate_release_dates()
        self.processing_times = self.generate_processing_times()

    def generate_machines(self):
        machines = pd.DataFrame(
            data=[[0.0, []] for _ in range(self.no_of_machines)],
            columns=["processing_time", "assigned_jobs"],
        )
        return machines

    def generate_release_dates(self):
        release_dates = []

        if not release_dates:
            # Generating random release dates
            release_dates = np.random.randint(
                low=self.jobs_params["release_date"]["min"],
                high=self.jobs_params["release_date"]["max"] * self.no_of_jobs / 10,
                size=self.no_of_jobs,
            )
        release_dates = pd.DataFrame(data=release_dates, columns=["release_date"])

        return release_dates

    def generate_processing_times(self):
        processing_times = []

        if not processing_times:
            # Generating random processing times
            processing_times = np.random.randint(
                low=self.jobs_params["operation_processing_time"]["min"],
                high=self.jobs_params["operation_processing_time"]["max"],
                size=(self.no_of_machines, self.no_of_jobs),
            )
        processing_times = pd.DataFrame(processing_times)
        processing_times.name = "ProcessingTimes"
        return processing_times
