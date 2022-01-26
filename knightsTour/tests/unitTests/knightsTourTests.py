import logging
import sys

import pytest
import pytest_asyncio

from knightsTour.board import(
    Board,
    Coordinate,
)
from knightsTour.exceptions import(
    InvalidLocationError,
)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

@pytest_asyncio.fixture()
def kboard():
    board = Board()
    yield board

@pytest_asyncio.fixture()
def startLoc():
    coordinate = Coordinate(0, 0)
    yield coordinate

def instantiateBoard8x8Test(kboard):
    logger.info("board\n%s", kboard)
    assert len(kboard.board) == 8
    for row in kboard.board:
        assert len(row) == 8

@pytest.mark.parametrize("coordinate", [Coordinate(1,2), Coordinate(0,0), Coordinate(4,7)])
def checkValidBoardLocationTest(coordinate, kboard):
    kboard.onBoard(coordinate)

@pytest.mark.parametrize("coordinate", [Coordinate(0,20), Coordinate(8,8), Coordinate(10,7)])
def checkInvalidBoardLocationTest(coordinate, kboard):
    with pytest.raises(InvalidLocationError):
        kboard.onBoard(coordinate)

@pytest.mark.parametrize("coordinate", [Coordinate(1,2), Coordinate(0,0), Coordinate(4,7)])
def checkSquareAvailableTest(coordinate, kboard):
    kboard.available(coordinate)

@pytest.mark.parametrize("coordinates", [(Coordinate(1,2), Coordinate(0,0), Coordinate(4,7))])
def moveToSquareTest(coordinates, kboard):
    for coordinate in coordinates:
        logger.info("coordinate=%s", coordinate)
        kboard.move(coordinate)
        assert not kboard.available(coordinate)
    logger.info("board\n%s", kboard)

def wknightTest(kboard, startLoc):
    wknight = kboard.start(startLoc)
    assert not kboard.available(startLoc)
    assert wknight.path == [startLoc]
