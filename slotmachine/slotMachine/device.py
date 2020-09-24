import random

class SlotMachine:
    def __init__(self, symbols: list, wheels: int) -> None:
        self.symbols = symbols
        self.wheels = wheels

    def pullHandle(self)->list:
        return [random.choice(self.symbols) for i in range(self.wheels)]

    # {i:MyList.count(i) for i in MyList}
