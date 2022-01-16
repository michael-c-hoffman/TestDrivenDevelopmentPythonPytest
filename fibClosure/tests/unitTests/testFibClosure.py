from fibClosure import fib


def test_fib(data_fib) -> None:
    assert fib.fibx(data_fib[0]) == data_fib[1]
