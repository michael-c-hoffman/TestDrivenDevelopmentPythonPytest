from typing import Any

import pytest

from filostack import Filostack


class TestFiloStack:
    @pytest.fixture
    def filostack(self, data_stack) -> Filostack:
        filostack = Filostack()
        yield Filostack()

    def test_CreateFilostack(self, filostack) -> None:
        assert filostack

    def test_PushItem(self, filostack, data_stack) -> None:
        filostack.push(data_stack)

    def test_PopItem(self, filostack, data_stack) -> None:
        filostack.push(data_stack)
        assert type(filostack.pop())

    def test_LengthFilostack(self, filostack, data_stack) -> None:
        filostack.push(data_stack)
        filostack.push(data_stack)
        assert(isinstance(filostack.length(), int))
        assert(filostack.length() == 2)

    def test_PopEmptyStack(self, filostack) -> None:
        with pytest.raises(IndexError):
            filostack.pop()

    def test_MultiplePops(self, filostack, data_stack) -> None:
        filostack.push(data_stack)
        filostack.push(data_stack)
        assert type(filostack.pop())
        assert type(filostack.pop())

    def test_PushPopValue(self, filostack, data_stack) -> None:
        filostack.push(data_stack)
        assert filostack.pop() == data_stack
