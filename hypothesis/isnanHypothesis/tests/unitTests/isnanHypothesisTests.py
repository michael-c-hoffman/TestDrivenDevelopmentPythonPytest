from hypothesis import(
    event,
    given,
    settings,
    Verbosity,
    strategies as st
)

import pytest

@settings(verbosity=Verbosity.verbose)
@given(
    st.integers(),
    st.integers()
)
def intsAreCommutativeTest(x,y):
    assert x + y == y + x
