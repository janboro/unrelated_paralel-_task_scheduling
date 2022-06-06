load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "test_analysis",
    srcs = ["test_analysis.py"],
    deps = [
        "//data_type:data_types",
        "//third_party:numpy",
        "//third_party:pandas",
        "//third_party:scipy",
    ],
)
