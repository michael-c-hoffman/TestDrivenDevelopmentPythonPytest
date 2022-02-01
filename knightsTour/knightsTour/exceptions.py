"""
Exceptions for knightsTour
"""


class KnightsTourError(Exception):
    """ Base Exception for knightsTour """

class InvalidBoardSizeError(KnightsTourError):
    """ Invalid Board Size Specified """

class InvalidLocationError(KnightsTourError):
    """ Invalid Location on Board """

class NoMoreMovesError(KnightsTourError):
    """ No more move Locations on Board """
