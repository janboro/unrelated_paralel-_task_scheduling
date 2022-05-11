load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "task_scheduling_runner",
    srcs = ["task_scheduling_runner.py"],
    deps = [
        "//algorithms:particle_swarm_optimization",
        "//task_generator:task_scheduling_generator",
    ],
)
