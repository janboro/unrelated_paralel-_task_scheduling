load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "local_search",
    srcs = ["local_search.py"],
    deps = [
        "//third_party:numpy",
        "//utils",
    ],
)

py_library(
    name = "operators",
    srcs = ["operators.py"],
    deps = [
        ":random_solution",
        "//third_party:numpy",
        "//utils",
    ],
)

py_library(
    name = "particle_swarm_optimization",
    srcs = ["particle_swarm_optimization.py"],
    deps = [
        ":local_search",
        ":operators",
        ":random_solution",
        ":shortest_release_date",
        "//data_type:data_types",
        "//third_party:numpy",
        "//utils",
    ],
)

py_library(
    name = "random_solution",
    srcs = ["random_solution.py"],
    deps = [
        "//utils",
    ],
)

py_library(
    name = "simulated_annealing",
    srcs = ["simulated_annealing.py"],
    deps = [
        ":local_search",
        ":random_solution",
        "//data_type:data_types",
        "//third_party:pandas",
        "//utils",
    ],
)

py_library(
    name = "shortest_release_date",
    srcs = ["shortest_release_date.py"],
    deps = [
        "//third_party:pandas",
        "//utils",
    ],
)
