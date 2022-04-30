from abc import abstractmethod
from typing import Protocol, List

class PColor(Protocol):
    @abstractmethod
    def draw(self) -> str:
        pass
        # draw something
    def complex_method(self) -> int:
        pass
        # some complex code here

class NiceColor(PColor):
    def draw(self) -> str:
        return "deep blue"

class BadColor(PColor):
    def draw(self) -> str:
        return super().draw()  # Error, no default implementation

class ImplicitColor:   # Note no 'PColor' base here
    def draw(self) -> str:
        return "probably gray"
    def complex_method(self) -> int:
        pass
        # class needs to implement this

nice: NiceColor = NiceColor()
another: ImplicitColor = ImplicitColor()

def represent(c: PColor) -> None:
    print(c.draw(), c.complex_method())

represent(nice) # OK
represent(another) # Also OK
