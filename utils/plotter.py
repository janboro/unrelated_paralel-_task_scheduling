import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn")
sns.set_palette(sns.color_palette("Blues"))


def gantt_plot(scheduling_solution, title, plot_label=True):
    plt.figure()
    plt.title(title)
    for machine in scheduling_solution.machines.itertuples():
        processing_time = 0
        for job in machine.assigned_jobs:
            start_time = max(processing_time, scheduling_solution.jobs.loc[job, "release_date"])
            end_time = start_time + scheduling_solution.processing_times.loc[machine.Index, job]
            processing_time = end_time

            plt.barh(
                y=f"M{machine.Index}",
                left=start_time,
                width=end_time - start_time,
                edgecolor="black",
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


def plot_jobs(scheduling_solution):
    plt.figure()
    plt.title("Jobs release dates")
    min_processing_time = scheduling_solution.processing_times.min()
    sorted_jobs = scheduling_solution.jobs.sort_values(["release_date"])
    for job in sorted_jobs.itertuples():
        plt.barh(
            y=f"J{job.Index}",
            left=job.release_date,
            width=min_processing_time.iloc[job.Index],
            color="#006DB2",
            edgecolor="black",
        )
    plt.gca().invert_yaxis()
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.xlim(left=0)
    plt.show()
