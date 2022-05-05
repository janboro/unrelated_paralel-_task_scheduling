import numpy as np


def sphere(values: np.ndarray):
    return np.sum(np.power(values, 2))


def parabole(values: np.ndarray):
    return 5 * values[0] ** 2 + 3 * values[1] + values[2]
