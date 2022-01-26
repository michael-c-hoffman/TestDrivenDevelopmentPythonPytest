"""
Exceptions for knightsTour
"""


class KnightsTourError(Exception):
    """ Base Exception for knightsTour """


class InvalidLocationError(KnightsTourError):
    """ Invalid Location on Board """
