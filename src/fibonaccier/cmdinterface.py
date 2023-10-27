from .fibonaccier import Fibonaccier


class CmdInterface:
    TRIES = 5
    PROMPT = "Please input the index number of the desired Fibonacci element: "
    NOT_INT = "The given input was not a valid integer."
    BELOW_ONE = "Values below 1 are not accepted."

    @staticmethod
    def main():
        for current_try in range(CmdInterface.TRIES):
            try:
                desired_index = int(input(CmdInterface.PROMPT))
            except ValueError:
                print(CmdInterface.NOT_INT)
                continue
            if desired_index > 1:
                result, run_time, call_number = Fibonaccier.do_concurrent_calculations(desired_index)
                break
            else:
                print(CmdInterface.BELOW_ONE)
        else:
            print(f"Not a valid integer in {CmdInterface.TRIES} tries? I see, you are doing some exploratory testing. ;)")
            return
        print(f"The {desired_index}. element of the Fibonacci sequence is: {result}")
        print(f"The faster call was call #{call_number}. It finished under {run_time:.4f} seconds.")
