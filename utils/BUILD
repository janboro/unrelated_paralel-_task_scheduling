load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "singleton",
    srcs = ["singleton_meta.py"],
)

py_library(
    name = "plotter",
    srcs = ["plotter.py"],
    deps = [
        "//third_party:matplotlib",
        "//third_party:numpy",
    ],
)
