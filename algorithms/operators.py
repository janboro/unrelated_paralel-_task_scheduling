from typing import List
from itertools import groupby
import numpy as np
from algorithms.shortest_release_date import ShortestReleaseDates


class Operators:
    def __init__(self):
        self.SRD = ShortestReleaseDates()

    @staticmethod
    def vectorize_solution(machines):
        solution_vector = []
        for jobs in machines["assigned_jobs"]:
            if len(jobs) > 0:
                for job in jobs:
                    solution_vector.append(job)
            else:
                solution_vector.append(None)
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
        """Sorting based on a bubble sort"""
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] is None and arr[j + 1] is not None and arr[j + 1] != "*":
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def _substractor(arr_A: List, arr_B: List):
        result = []
        buffer = []
        for i, j in zip(arr_A, arr_B):
            if i == j and i != "*":
                result.append(None)
                buffer.append(i)
            else:
                result.append(i)
        return result, buffer

    def substract(self, arr_A: List, arr_B: List):
        substraction, buffer = self._substractor(arr_A, arr_B)
        substraction = self._sort_substraction(substraction)
        substraction = self._fill_missing_fields(substraction, buffer)
        return substraction

    @staticmethod
    def get_grouped_solution(arr: List):
        return [list(group) for k, group in groupby(arr, lambda x: x == "*") if not k]

    def _get_multiplication_vector(self, arr_A: List, arr_B: List) -> List[List]:
        result = []
        for i in range(len(arr_A)):
            if arr_B[i] == "*":
                result.append("*")
            elif arr_A[i] == 1:
                result.append(arr_B[i])
            else:
                result.append(None)
        return result

    def multiply(self, arr_A: List, arr_B: List, scheduling_problem):
        multiplication_vector = self._get_multiplication_vector(arr_A=arr_A, arr_B=arr_B)
        assigned_jobs = self.get_grouped_solution(multiplication_vector)

        _, scheduled_jobs = self.SRD.initialize_solution(
            scheduling_problem=scheduling_problem,
            grouped_vectorized_solution=assigned_jobs,
        )
        self.SRD.assign_jobs(scheduling_problem=scheduling_problem, scheduled_jobs=scheduled_jobs)

        return scheduled_jobs

    def add(self, arr_A: List, arr_B: List):
        grouped_solution = self.get_grouped_solution(arr=arr_A)
        group_to_select = np.random.randint(low=0, high=len(grouped_solution))

        result = []
        buffer = []
        for i in range(len(grouped_solution)):
            for job in grouped_solution[i]:
                if i == group_to_select:
                    result.append(job)
                else:
                    result.append(None)
                    buffer.append(job)
            result.append("*")
        result.pop()

        jobs_to_schedule = [value for value in arr_B if value in buffer]

        for i in range(len(result)):
            if result[i] is None:
                result[i] = jobs_to_schedule.pop(0)
        return result
