from typing import Any, Callable, Tuple
from timeit import default_timer


def stopwatch(function: Callable):
    """Measures a call and returns the measured value as well as the original return value.

    Args:
        function (Callable): The function to decorate.
    """
    async def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        start = default_timer()
        return_value = await function(*args, *kwargs)
        result = default_timer() - start
        return return_value, result
    return wrapper
