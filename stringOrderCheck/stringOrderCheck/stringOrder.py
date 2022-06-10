"""
library for finding string order
"""
import logging
import re

logger = logging.getLogger(__name__)


def orderScan(inputstr: str, orderstr: str) -> bool:
    """
    perform order scan on string given inputstr and orderstr
    """
    ordered = True
    indices = orderIndices(inputstr, orderstr)
    # if empty indices the required order characters not found return false
    if len(indices) == 0:
        ordered = False
    for index in indices:
        logger.debug(f"start check from={inputstr[index]}")
        # get the next character in ordered list
        nextCharacter = nextChar(orderstr, inputstr[index])
        logger.debug(f"checking for nextCharacter={nextCharacter}")
        # check if inputstr is still ordered
        ordered = checkOrder(inputstr[index:], orderstr, nextCharacter)
        logger.debug(f"ordered={ordered}")
        if not ordered:
            # string is not ordered set to false and break from lop
            ordered = False
            break
    return ordered


def nextChar(orderstr: str, char: str):
    """
    find what the next character to search for is
    """
    nextchar = ""
    try:
        # get current character + 1 account for index out of range
        nextchar = orderstr[orderstr.find(char) + 1]
    except IndexError:
        logger.debug("next character doesn't matter past order list")
    return nextchar


def orderIndices(inputstr: str, orderstr: str) -> list:
    """
    return a list of indices in inputstr that match characters in orderstr
    if character in orderstr is not found return empyt string
    """
    indices: list = []
    for char in orderstr:
        # for each character in ordered string get indices from inputstr
        search = [i.start() for i in re.finditer(char, inputstr)]
        if len(search) == 0:
            logger.debug(f"char {char} not found")
            # set indices to empty list for character not found and break
            indices = []
            break
        indices.extend(search)
    return indices


def checkOrder(inputstr: str, orderstr: str, nextchar: str) -> bool:
    """
    given an input string check if next character is not in orderstr or
    next character is the nextchar
    """
    order = False
    if nextchar == "":
        order = True
    else:
        for char in inputstr:
            if char not in orderstr:
                continue
            if char == nextchar:
                order = True
                break
    return order
