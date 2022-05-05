load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "config_handler",
    srcs = [
        "config_handler.py",
    ],
    data = [
        "parameters.yaml",
    ],
    deps = [
        "//third_party:pyyaml",
        "//utils:singleton",
    ],
)
