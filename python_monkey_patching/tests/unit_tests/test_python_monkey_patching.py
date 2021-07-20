import python_monkey_patching import fib


def test_fib(monkeypatch) -> None:
    def mock_fib(x):
        return 11

    monkeypatch.setattr(fib, 'fib', mock_fib)
    assert fib.fib(11) == 11
