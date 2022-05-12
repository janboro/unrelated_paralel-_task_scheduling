import matplotlib.pyplot as plt
import numpy as np


def generate_color():
    return tuple(np.random.randint(256, size=3) / 256)


def gantt_plot(scheduling_solution, title, plot_label=True):
    plt.figure()
    plt.title(title)
    for machine in scheduling_solution.machines.itertuples():
        processing_time = 0
        for job in machine.assigned_jobs:
            print(f"Machine: {machine.Index}")
            print(f"Job: {job}")
            start_time = max(processing_time, scheduling_solution.jobs.loc[job, "release_date"])
            end_time = start_time + scheduling_solution.processing_times.loc[machine.Index, job]
            processing_time = end_time
            color = generate_color()

            plt.barh(
                y=f"M{machine.Index}",
                left=start_time,
                width=end_time - start_time,
                color=color,
                label=f"J{job}",
            )

    plt.gca().invert_yaxis()

    # Plotting handles
    handles, labels = plt.gca().get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    if plot_label:
        plt.legend(handle_list, label_list)
    plt.xlim(left=0)
    plt.show()
