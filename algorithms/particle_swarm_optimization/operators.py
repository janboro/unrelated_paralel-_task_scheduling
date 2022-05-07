from typing import List
import numpy as np


class Operators:
    @staticmethod
    def vectorize_solution(machines):
        solution_vector = []
        for jobs in machines["assigned_jobs"]:
            for job in jobs:
                solution_vector.append(job)
            solution_vector.append("*")
        solution_vector.pop()
        return solution_vector

    @staticmethod
    def _fill_missing_fields(arr: List, buffer: List):
        for i in range(len(arr)):
            if arr[i] is None:
                arr[i] = buffer.pop(0)
        return arr

    @staticmethod
    def _sort_substraction(arr: List):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] is None and arr[j + 1] is not None and arr[j + 1] != "*":
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def _substractor(a: List, b: List):
        result = []
        buffer = []
        for i, j in zip(a, b):
            if i == j and i != "*":
                result.append(None)
                buffer.append(i)
            else:
                result.append(i)
        return result, buffer

    def substract(self, A, B):
        substraction, buffer = self._substractor(A, B)
        substraction = self._sort_substraction(substraction)
        substraction = self._fill_missing_fields(substraction, buffer)
        return substraction

    def multiply(self, A):
        B = list(np.random.binomial(n=1, p=0.5, size=len(A)))
        result = [a * b if type(a) == int else "*" for a, b in zip(A, B)]
        result = list(filter(lambda x: x != 0, result))  # remove 0 from result vector
        return result

    def add(self):
        pass
