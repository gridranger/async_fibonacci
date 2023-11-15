from unittest import TestCase
from unittest.mock import call, Mock, patch

from src.fibonaccier.cmdinterface import CmdInterface


class TestCmdInterface(TestCase):

    @patch("builtins.input", side_effect=["a", 0, 3])
    @patch("builtins.print")
    @patch("src.fibonaccier.fibonaccier.Fibonaccier.do_concurrent_calculations", return_value=(3, 0.1, 2))
    def test_main(self, do_concurrent_calculations: Mock, mocked_print: Mock, mocked_input: Mock):
        CmdInterface.main()
        mocked_print.assert_has_calls([call(CmdInterface.NOT_INT),
                                       call(CmdInterface.BELOW_ONE),
                                       call("The 3. element of the Fibonacci sequence is: 3"),
                                       call("The faster call was call #2. It finished under 0.1000 seconds.")])
        assert mocked_input.call_count == 3
        do_concurrent_calculations.assert_called_once_with(3)

    @patch("builtins.input", side_effect=range(-4, 1))
    @patch("builtins.print")
    def test_main_no_valid_inputs(self, mocked_print: Mock, mocked_input: Mock):
        CmdInterface.main()
        assert mocked_input.call_count == CmdInterface.TRIES
        mocked_print.assert_called_with("Not a valid integer in 5 tries? I see, you are doing some exploratory testing. ;)")
