from asyncio import run
from unittest import TestCase
from unittest.mock import call, MagicMock, Mock, patch
from src.fibonaccier.fibonaccier import Fibonaccier


class AsyncSleepMock(MagicMock):
    async def __call__(self, sleep_time):
        return super(AsyncSleepMock, self).__call__(sleep_time)


class TestFibonaccier(TestCase):

    def test_calculate_already_known(self):
        assert Fibonaccier._calculate(1) == 1

    def test_calculate_new(self):
        assert Fibonaccier._calculate(50) == 12586269025
        assert len(Fibonaccier._cache) == 51

    @patch.object(Fibonaccier, "_calculate", return_value=55)
    @patch("src.fibonaccier.fibonaccier.async_sleep", new_callable=AsyncSleepMock)
    def test_async_calculate(self, sleep: AsyncSleepMock, calculate: Mock):
        result = run(Fibonaccier._async_calculate(10))
        assert result[0] == calculate.return_value
        assert 0 < result[1] < 1
        sleep.assert_called()
        calculate.assert_called_once_with(10)

    @patch.object(Fibonaccier, "_async_calculate", return_value=(55, 0.1))
    def test__do_concurrent_calculations(self, async_calculate: Mock):
        assert run(Fibonaccier._do_concurrent_calculations(10))
        async_calculate.assert_has_calls([call(10)] * 2)

    @patch.object(Fibonaccier, "_do_concurrent_calculations", return_value=(89, 0.1, 1))
    def test_do_concurrent_calculations(self, private_do_concurrent_calculations):
        assert Fibonaccier.do_concurrent_calculations(11) == private_do_concurrent_calculations.return_value
