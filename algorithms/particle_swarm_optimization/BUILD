load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "particle_swarm_optimization",
    srcs = ["particle_swarm_optimization.py"],
    deps = [
        "//data_type:data_types",
        "//third_party:numpy",
    ],
)

py_library(
    name = "operators",
    srcs = ["operators.py"],
    deps = [
        "//third_party:numpy",
    ],
)
