from typing import List
from itertools import groupby
from algorithms.shortest_release_date.shortest_release_date import ShortestReleaseDates


class Operators:
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

    def multiply(self, A, B, problem):
        result = []
        for i in range(len(A)):
            if B[i] == "*":
                result.append("*")
            elif A[i] == 1:
                result.append(B[i])
            else:
                result.append(None)
        assigned_jobs = [list(group) for k, group in groupby(result, lambda x: x == "*") if not k]

        scheduled_jobs = []
        for machine_index, jobs in zip(problem.machines.index, assigned_jobs):
            problem.machines.loc[machine_index, "assigned_jobs"].clear()
            problem.machines.loc[machine_index, "processing_time"] = 0.0
            for job in jobs:
                if job == "*":
                    break
                elif job is not None:
                    problem.machines.loc[machine_index, "assigned_jobs"].append(job)
                    problem.machines.loc[machine_index, "processing_time"] = (
                        max(
                            problem.machines.loc[machine_index, "processing_time"],
                            problem.jobs.loc[job, "release_date"],
                        )
                        + problem.processing_times.loc[machine_index, job]
                    )
                    scheduled_jobs.append(job)

        shortest_relese_dates = ShortestReleaseDates(problem=problem, scheduled_jobs=scheduled_jobs)
        shortest_relese_dates.assign_jobs()

        return result
