import logging
import sys

import pytest
import pytest_asyncio

from knightsTour.game import(
    Knight,
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

@pytest.mark.parametrize("requestedSize", [8, 4, 9])
def instantiateBoardSizeTest(requestedSize):
    kboard = Board(requestedSize)
    logger.info("board\n%s", kboard)
    assert kboard.size == requestedSize

@pytest.mark.parametrize("coordinate", [Coordinate(1,2), Coordinate(0,0), Coordinate(4,7),])
def checkValidBoardLocationTest(coordinate, kboard):
    kboard.onBoard(coordinate)

@pytest.mark.parametrize("coordinate", [Coordinate(0,20), Coordinate(8,8), Coordinate(10,7), Coordinate(-1, 0), Coordinate(0, -1)])
def checkInvalidBoardLocationTest(coordinate, kboard):
    with pytest.raises(InvalidLocationError):
        kboard.onBoard(coordinate)

@pytest.mark.parametrize("coordinate", [Coordinate(1,2), Coordinate(0,0), Coordinate(4,7)])
def checkSquareAvailableTest(coordinate, kboard):
    assert kboard.available(coordinate)

@pytest.mark.parametrize("coordinate", [Coordinate(1,2), Coordinate(0,0), Coordinate(4,7)])
def checkSquareUnavailableTest(coordinate, kboard):
    kboard.move(coordinate)
    assert not kboard.available(coordinate)

@pytest.mark.parametrize("coordinates", [(Coordinate(1,2), Coordinate(0,0), Coordinate(4,7))])
def moveToSquareTest(coordinates, kboard):
    for coordinate in coordinates:
        logger.info("coordinate=%s", coordinate)
        kboard.move(coordinate)
        assert not kboard.available(coordinate)
    logger.info("board\n%s", kboard)

def instantiateWhiteKnightTest(kboard, startLoc):
    wknight = Knight(startLoc, kboard)
    assert isinstance(wknight, Knight)
    assert wknight.path == [startLoc]

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(2, 1))])
def knightMoveLeftUpTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.leftUp()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(1, 2))])
def knightMoveUpLeftTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.upLeft()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(1, 4))])
def knightMoveUpRightTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.upRight()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(2, 5))])
def knightMoveRightUpTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.rightUp()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(4, 1))])
def knightMoveLeftDownTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.leftDown()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(5, 2))])
def knightMoveDownLeftTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.downLeft()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(5, 4))])
def knightMoveDownRightTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.downRight()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(4, 5))])
def knightMoveRightDownTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.rightDown()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(3,3), Coordinate(1, 2))])
def knightFirstMoveUpLeftTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.nextMove()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinateStart, coordinateExpected", [(Coordinate(0,0), Coordinate(1, 2))])
def knightFirstMoveLoopToRightDownTest(kboard, coordinateStart, coordinateExpected):
    wknight = Knight(coordinateStart, kboard)
    location = wknight.nextMove()
    logger.info("board\n%s", wknight.board)
    assert location == coordinateExpected

@pytest.mark.parametrize("coordinates", [(
    Coordinate(3,3),
    Coordinate(1,2),
    Coordinate(1,4),
    Coordinate(2,1),
    Coordinate(2,5),
    Coordinate(4,1),
    Coordinate(5,2),
    Coordinate(5,4),
    Coordinate(4,5),
)])
def noNextMovesTest(kboard, coordinates):
    kboard = Board()
    for coordinate in coordinates[1:]:
        kboard.move(coordinate)
    logger.info("board before moves\n%s", kboard)

    wknight = Knight(coordinates[0], kboard)
    logger.info("board\n%s", kboard)
    with pytest.raises(InvalidLocationError) as error:
        wknight.nextMove()
    logger.info("knight path=%s", wknight.path)
