from typing import List
import numpy as np


class Operators:
    def _fill_missing_fields(self, arr: List, buffer: List):
        for i in range(len(arr)):
            if arr[i] is None:
                arr[i] = buffer.pop(0)
        return arr

    def _sort_substraction(self, arr: List):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] is None and arr[j + 1] is not None and arr[j + 1] != "*":
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def _substractor(self, a: List, b: List):
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
        print(list(np.random.binomial(n=1, p=0.5, size=len(A))))
        print(A)

    def add(self):
        pass
