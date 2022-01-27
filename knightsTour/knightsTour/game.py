import logging
import sys

from dataclasses import dataclass
from typing import Optional

from knightsTour.exceptions import (
    InvalidLocationError,
    InvalidBoardSizeError,
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


class Board:
    """ define type of board and moves """
    def __init__(self, size: int=8) -> None:
        # initialize 2d 8x8 matrix for board
        self.size = size
        self.__board = [
            [0] * self.size
            for i in range(self.size)
        ]

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: int):
        if value < 0:
            raise InvalidBoardSizeError
        self.__size = value

    def __repr__(self):
        string = ""
        for row in self.__board:
            string += f"{row}\n"
        return string

    def complete(self) -> bool:
        boardComplete = False
        for row in self.__board:
            if row != [1] * self.__size:
                break
        else:
            boardComplete = True
        return boardComplete

    def onBoard(self, location: Coordinate) -> bool:
        """ check if move is on the board """
        try:
            if location.x < 0 or location.y < 0:
                # a negative value means we are off the board
                raise IndexError
            self.__board[location.x][location.y]
            return True
        except IndexError as error:
            raise InvalidLocationError from error

    def available(self, location: Coordinate) -> bool:
        """ check if square is available """
        try:
            available = False
            if self.__board[location.x][location.y] == 0:
                available = True
        except IndexError as error:
            raise InvalidLocationError from error
        return available

    def move(self, location: Coordinate) -> bool:
        try:
            move = False
            if self.onBoard(location) and self.available(location):
                self.__board[location.x][location.y] = 1
                move = True
            return move
        except IndexError:
            raise InvalidLocationError

    def unset(self, location: Coordinate) -> None:
        try:
            self.__board[location.x][location.y] = 0
        except IndexError as error:
            raise InvalidLocationError from error


class Knight:
    """ Define knight current location and moves """
    def __init__(self, start: Coordinate, board: Board) -> None:
        self.board = board
        # try to place piece onto board
        if not self.board.move(start):
            raise InvalidLocationError
        self.path: list[Coordinate] = [start]
        self.__moves = [
            self.upLeft,
            self.upRight,
            self.leftUp,
            self.leftDown,
            self.rightUp,
            self.rightDown,
            self.downLeft,
            self.downRight,
        ]

    def nextMove(self) -> Optional[Coordinate]:
        nextCoordinate = None
        for move in self.__moves:
            try:
                # call function from list of __moves
                nextCoordinate = move()
                break
            except InvalidLocationError:
                continue
        else:
            raise InvalidLocationError("no more moves to try")
        return nextCoordinate

    def upLeft(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x - 2
        newY = currentLocation.y - 1
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def upRight(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x - 2
        newY = currentLocation.y + 1
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def leftUp(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x - 1
        newY = currentLocation.y - 2
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def rightUp(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x - 1
        newY = currentLocation.y + 2
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def downLeft(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x + 2
        newY = currentLocation.y - 1
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def downRight(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x + 2
        newY = currentLocation.y + 1
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def leftDown(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x + 1
        newY = currentLocation.y - 2
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation

    def rightDown(self) -> Coordinate:
        currentLocation = self.path[-1]
        newX = currentLocation.x + 1
        newY = currentLocation.y + 2
        newLocation = Coordinate(newX, newY)
        if self.board.move(newLocation):
            self.path.append(newLocation)
        else:
            raise InvalidLocationError("upLeft not valid move on board")
        return newLocation
