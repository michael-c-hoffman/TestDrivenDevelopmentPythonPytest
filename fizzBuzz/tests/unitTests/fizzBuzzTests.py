from fizzBuzz.fizzbuzz import Fizzbuzz

import pytest

class FizzbuzzTest:
    @pytest.mark.parametrize("given, expected", [(1, "1"), (2, "2")])
    def return_number_for_integerTest(self, given, expected):
        assert Fizzbuzz.evaluate(given) == expected
    @pytest.mark.parametrize("given, expected", [(18, "fizz")])
    def should_return_fizz_for_threeTest(self, given, expected):
        assert Fizzbuzz.evaluate(given) == expected
    @pytest.mark.parametrize("given, expected", [(5, "buzz")])
    def should_return_buzz_for_fiveTest(self, given, expected):
        assert Fizzbuzz.evaluate(given) == expected
    @pytest.mark.parametrize("given, expected", [(15, "fizzbuzz"), (30, "fizzbuzz")])
    def should_return_fizzbuzz_for_15_and_30Test(self, given, expected):
        assert Fizzbuzz.evaluate(given) == expected
    @pytest.mark.parametrize("given, expected", [
        (
            range(1,21),
            "1\n"
            "2\n"
            "fizz\n"
            "4\n"
            "buzz\n"
            "fizz\n"
            "7\n"
            "8\n"
            "fizz\n"
            "buzz\n"
            "11\n"
            "fizz\n"
            "13\n"
            "14\n"
            "fizzbuzz\n"
            "16\n"
            "17\n"
            "fizz\n"
            "19\n"
            "buzz\n"
        )
    ])
    def fizbuzz_to_20Test(self, given, expected):
        assert Fizzbuzz.run(given) == expected
