from asyncio import gather, run, sleep as async_sleep
from random import random
from typing import Tuple

from .stopwatch import stopwatch


class Fibonaccier:
    _cache = [0, 1]

    @classmethod
    def _fib(cls, number: int) -> int:
        """Calculates and returns the requested element of the Fibonacci sequence.

        Args:
            number (int): The index of the element to return from the sequence.

        Returns:
            int: The requested element of the Fibonacci sequence.
        """
        while len(cls._cache) <= number:
            cls._cache.append(cls._cache[-2] + cls._cache[-1])
        return cls._cache[number]

    @staticmethod
    @stopwatch
    async def _async_calculate(number: int) -> int:
        """Executes the calculate method asynchronously with random wait inside it.

        Args:
            number (int): The index of the element to return from the sequence.

        Returns:
            int: The requested element of the Fibonacci sequence.
        """
        await async_sleep(random())
        return Fibonaccier._fib(number)

    @staticmethod
    async def _do_concurrent_calculations(number: int) -> Tuple[int, float, int]:
        """Executes the _async_calculate twice, then return the results.

        Args:
            number (int): The index of the element to return from the sequence.

        Returns:
            Tuple[int, float, int]: The result, the length of the run and number of the winner.
        """
        task_1 = Fibonaccier._async_calculate(number)
        task_2 = Fibonaccier._async_calculate(number)
        return_values_1, return_values_2 = await gather(task_1, task_2)
        result_1, run_time_1 = return_values_1
        result_2, run_time_2 = return_values_2
        return result_1, min(run_time_1, run_time_2), 1 if run_time_1 < run_time_2 else 2

    @staticmethod
    def do_concurrent_calculations(number: int) -> Tuple[int, float, int]:
        """Keeps the async world under the hood so the user interface don't need to care about it.

        Args:
            number (int): The index of the element to return from the sequence.

        Returns:
            Tuple[int, float, int]: The result, the length of the run and number of the winner.
        """
        return run(Fibonaccier._do_concurrent_calculations(number))
