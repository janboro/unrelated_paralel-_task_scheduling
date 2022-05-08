load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "operators",
    srcs = ["operators.py"],
    deps = [
        "//third_party:numpy",
    ],
)

py_library(
    name = "particle_swarm_optimization",
    srcs = ["particle_swarm_optimization.py"],
    deps = [
        "//data_type:data_types",
        "//third_party:numpy",
    ],
)

py_library(
    name = "shortest_release_date",
    srcs = ["shortest_release_date.py"],
    deps = [
        "//data_type:data_types",
        "//task_generator:task_scheduling_generator",
        "//third_party:numpy",
        "//third_party:pandas",
    ],
)
