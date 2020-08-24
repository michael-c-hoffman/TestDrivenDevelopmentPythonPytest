import fib


def test_fib(data_fib) -> None:
    assert fib.fib(data_fib[0]) == data_fib[1]
