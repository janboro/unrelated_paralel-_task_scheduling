load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "task_scheduling_generator",
    srcs = ["task_scheduling_generator.py"],
    deps = [
        "//config:config_handler",
        "//third_party:numpy",
        "//third_party:pandas",
    ],
)
