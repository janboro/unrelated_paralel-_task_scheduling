import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, no_of_jobs):
        self.no_of_jobs = no_of_jobs
        self.colors = self.generate_colors(no_of_jobs=no_of_jobs)

    def generate_colors(self, no_of_jobs):
        colors = []
        for _ in range(no_of_jobs):
            colors.append(tuple(np.random.randint(256, size=3) / 256))
        return colors

    def gantt_plot(self, machines, title):
        plt.figure()
        plt.title(title)
        for machine in machines.itertuples():
            for job in machine.assigned_jobs:
                plt.barh(
                    y=f"M{machine.Index}",
                    left=job["start_time"],
                    width=job["end_time"] - job["start_time"],
                    color=self.colors[job["job_index"]],
                    label=f"J{job['job_index']}",
                )

        plt.gca().invert_yaxis()

        # Plotting handles
        handles, labels = plt.gca().get_legend_handles_labels()
        handle_list, label_list = [], []
        for handle, label in zip(handles, labels):
            if label not in label_list:
                handle_list.append(handle)
                label_list.append(label)
        plt.legend(handle_list, label_list)
        plt.xlim(left=0)
        plt.show()

    def job_shop_gantt_plot(self, machines, title):
        plt.figure()
        plt.title(title)
        for machine in machines.itertuples():
            for operation in machine.assigned_jobs:
                print(operation)
                print(operation["job"])
                print(self.colors)
                print(self.colors[operation["job"]])
                plt.barh(
                    y=f"M{machine.Index}",
                    left=operation["start_time"],
                    width=operation["end_time"] - operation["start_time"],
                    color=self.colors[operation["job"]],
                    label=f"J{operation['job']}",
                )

        plt.gca().invert_yaxis()

        # Plotting handles
        handles, labels = plt.gca().get_legend_handles_labels()
        handle_list, label_list = [], []
        for handle, label in zip(handles, labels):
            if label not in label_list:
                handle_list.append(handle)
                label_list.append(label)
        plt.legend(handle_list, label_list)
        plt.xlim(left=0)
        plt.show()
