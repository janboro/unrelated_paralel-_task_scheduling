workspace(
    name = "unrelated_parallel_task_scheduling",
)

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_utils",
    sha256 = "8616f3beb416e3e0399b3c14eb9dcdf77239f12fdaeb9729449850329b99e989",
    strip_prefix = "bazel_utils-1.0.3",
    url = "https://github.com/jake-arkinstall/bazel_utils/archive/1.0.3.tar.gz",
)

http_archive(
    name = "rules_python",
    sha256 = "778197e26c5fbeb07ac2a2c5ae405b30f6cb7ad1f5510ea6fdac03bded96cc6f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_python/releases/download/0.2.0/rules_python-0.2.0.tar.gz",
        "https://github.com/bazelbuild/rules_python/releases/download/0.2.0/rules_python-0.2.0.tar.gz",
    ],
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "unrelated_parallel_task_scheduling_deps",
    requirements = "//third_party:requirements.txt",
)

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "59536e6ae64359b716ba9c46c39183403b01eabfbd57578e84398b4829ca499a",
    strip_prefix = "rules_docker-0.22.0",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.22.0/rules_docker-v0.22.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

load(
    "@io_bazel_rules_docker//python3:image.bzl",
    _py3_image_repos = "repositories",
)

_py3_image_repos()

container_repositories()

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)

container_pull(
    name = "ubuntu_python3",
    timeout = 1800,
    registry = "index.docker.io",
    repository = "nutshellhub/ubuntu_python3",
    tag = "latest",
)
