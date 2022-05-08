load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "task_scheduling_runner",
    srcs = ["task_scheduling_runner.py"],
    deps = [
        "//algorithms:local_search",
        "//algorithms:operators",
        "//algorithms:shortest_release_date",
        "//task_generator:task_scheduling_generator",
        "//third_party:numpy",
    ],
)
