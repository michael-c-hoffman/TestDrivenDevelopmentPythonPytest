import logging
import sys

from dataclasses import dataclass


from knightsTour.exceptions import(
    InvalidLocationError,
)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


@dataclass
class Coordinate:
    """ coordinate data class """
    x: int
    y: int


class Knight:
    """ Define knight current location and moves """
    def __init__(self, start: Coordinate):
        self.path: list[Coordinate] = [start]


class Board:
    """ define type of board and moves """
    def __init__(self):
        # initialize 2d 8x8 matrix for board
        self.board = [
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
        ]

    def __repr__(self):
        string = ""
        for row in self.board:
            string += f"{row}\n"
        return string

    def start(self, location: Coordinate):
        self.move(location)
        return Knight(location)

    def onBoard(self, location: Coordinate):
        """ check if move is on the board """
        try:
            self.board[location.x][location.y]
            return True
        except IndexError as error:
            raise InvalidLocationError from error

    def available(self, location: Coordinate):
        """ check if square is available """
        try:
            available = False
            if self.board[location.x][location.y] == 0:
                available = True
            return available
        except IndexError as error:
            raise InvalidLocationError from error

    def move(self, location: Coordinate):
        if self.onBoard(location) and self.available(location):
            self.board[location.x][location.y] = 1
