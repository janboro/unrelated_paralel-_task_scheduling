load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "pso_runner",
    srcs = ["pso_runner.py"],
    deps = [
        "//algorithms:particle_swarm_optimization",
        "//data_type:data_types",
        "//task_generator:task_scheduling_generator",
        "//third_party:matplotlib",
        "//third_party:ptvsd",
    ],
)

py_binary(
    name = "simulated_annealing_runner",
    srcs = ["simulated_annealing_runner.py"],
    deps = [
        "//algorithms:shortest_release_date",
        "//algorithms:simulated_annealing",
        "//task_generator:task_scheduling_generator",
        "//third_party:matplotlib",
        "//utils",
        "//utils:plotter",
    ],
)

py_binary(
    name = "run_all",
    srcs = ["run_all.py"],
    deps = [
        "//algorithms:particle_swarm_optimization",
        "//algorithms:shortest_release_date",
        "//algorithms:simulated_annealing",
        "//data_type:data_types",
        "//task_generator:task_scheduling_generator",
        "//third_party:matplotlib",
        "//utils",
        "//utils:plotter",
    ],
)
