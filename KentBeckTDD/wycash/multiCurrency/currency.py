"""
class to implement dollar
"""
from __future__ import annotations
import datetime
import logging


from forex_python.converter import get_rate
from enum import Enum
from abc import (
    ABC,
    abstractmethod
)

logger = logging.getLogger(__name__)

class Currency(Enum):
    """
    Enum for difference currencies
    """
    USD = "USD"
    EUR = "EUR"

class Money():
    """
    General Money Class
    """
    def __init__(self, amount: float, currency: Currency) -> None:
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return round(self.__amount, 2)

    @amount.setter
    def amount(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"Invalid Amount ({value})")
        self.__amount = value

    def __repr__(self):
        return f'{self.currency}({{"ID": {id(self)}, "amount": {self.amount}}})'

    def __eq__(self, equality: Money) -> bool:
        logger.debug("self=%s", self.amount)
        logger.debug("equality=%s", equality.amount)

        cur = self.currency == equality.currency
        amount = self.amount == equality.amount
        return cur and amount

    def __mul__(self, multiplier: Money) -> Money:
        # get Current Currency Rates
        exchange = round(get_rate(multiplier.currency.value, self.currency.value), 2)
        multipland = multiplier.amount * exchange
        return Money(self.amount * multipland, self.currency)

    def __add__(self, adder: Money) -> Money:
        # get Current Currency Rates
        exchange = round(get_rate(adder.currency.value, self.currency.value), 2)
        addipland = adder.amount * exchange
        return Money(self.amount + addipland, self.currency)
