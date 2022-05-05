from os import path
import yaml
from utils.singleton_meta import SingletonMeta


class ParametersHandler(metaclass=SingletonMeta):
    current_directory = path.dirname(path.realpath(__file__))
    file_path = path.normpath(path.join(current_directory, "parameters.yaml"))
    with open(file_path, "r") as f:
        handler = yaml.safe_load(f)
