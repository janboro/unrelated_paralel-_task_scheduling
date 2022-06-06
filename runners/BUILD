load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "run_tests",
    srcs = ["run_tests.py"],
    data = [":testing_results.csv"],
    deps = [
        "//algorithms:particle_swarm_optimization",
        "//algorithms:shortest_release_date",
        "//algorithms:simulated_annealing",
        "//data_type:data_types",
        "//task_generator:task_scheduling_generator",
        "//utils",
        "//utils:plotter",
    ],
)

py_binary(
    name = "run_srd",
    srcs = ["run_srd.py"],
    deps = [
        "//algorithms:shortest_release_date",
        "//task_generator:task_scheduling_generator",
        "//utils",
        "//utils:plotter",
    ],
)

py_binary(
    name = "run_sa",
    srcs = ["run_sa.py"],
    deps = [
        "//algorithms:simulated_annealing",
        "//task_generator:task_scheduling_generator",
        "//third_party:matplotlib",
        "//utils",
        "//utils:plotter",
    ],
)

py_binary(
    name = "run_pso",
    srcs = ["run_pso.py"],
    deps = [
        "//algorithms:particle_swarm_optimization",
        "//data_type:data_types",
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
