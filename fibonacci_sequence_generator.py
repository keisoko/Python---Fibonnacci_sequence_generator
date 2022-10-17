"""Fibonacci Sequence Generator"""

import pprint
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class ConstantsNamespace:
    """Class to hold constants"""

    START_OF_SEQUENCE: int = 1


constants = ConstantsNamespace()


class StartOfSequenceLessThanOne(Exception):
    """Custom exception class"""

    def __str__(self):
        return "START_OF_SEQUENCE must be 1"


@lru_cache(maxsize=5)
def fibonacci_sequence_generator(end: int) -> list[int]:
    """Generates a list of fibonacci numbers from a given range."""

    if constants.START_OF_SEQUENCE < 1:
        raise StartOfSequenceLessThanOne()

    fib_list = [0, 1]
    fib_list.extend(
        fib_list[-1] + fib_list[-2] for _ in range(constants.START_OF_SEQUENCE, end + 1)
    )
    fib_list.insert(0, len(fib_list))

    return fib_list


def execute_main() -> None:

    custom_printer = pprint.PrettyPrinter(underscore_numbers=True, width=200)

    custom_printer.pprint(fibonacci_sequence_generator(end=19))
    custom_printer.pprint(fibonacci_sequence_generator(end=22))
    custom_printer.pprint(fibonacci_sequence_generator(end=24))


if __name__ == "__main__":
    execute_main()
