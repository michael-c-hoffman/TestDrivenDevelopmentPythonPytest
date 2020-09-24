import pytest

from slotMachine.device import SlotMachine

@pytest.fixture(params=[(3, ["7", "bar", "cherry", "mellon", "bar", "cherry", "mellon", "cherry", "mellon", "mellon"]), (4, ["blue", "yellow", "red"])])
def NewSlotMachine(request):
    slotMachine = SlotMachine(wheels=request.param[0], symbols=request.param[1])
    yield slotMachine
    # tear down code will go here

def test_Instantiation(NewSlotMachine):
    assert NewSlotMachine

def test_PullHandle(NewSlotMachine):
    results = NewSlotMachine.pullHandle()
    assert isinstance(results, list)
    assert len(results) == NewSlotMachine.wheels
    for result in results:
        assert result in NewSlotMachine.symbols
    print(results)
