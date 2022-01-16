from math import sqrt
from hypothesis import (
        settings,
        Verbosity,
        given,
        strategies as st,
        )
from fib.fib import fib

@settings(verbosity=Verbosity.verbose)
@given(st.integers(min_value=0, max_value=1000))
def fibTest(n: int) -> None:
    assert isinstance(fib(n), int)
