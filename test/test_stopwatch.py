from asyncio import run
from unittest import TestCase

from src.fibonaccier.stopwatch import stopwatch


class TestStopwatch(TestCase):

    @staticmethod
    async def mock_function():
        return 1

    def test_stopwatch(self):
        result = run(stopwatch(self.mock_function)())
        assert result[0] == 1
        assert 0 < result[1] < 0.1
