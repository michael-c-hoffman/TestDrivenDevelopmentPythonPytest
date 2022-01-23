"""
class to implement dollar
"""
from __future__ import annotations

import logging
from enum import Enum

from forex_python import converter  # type: ignore

logger = logging.getLogger(__name__)


class Currency(Enum):
    """
    Enum for difference currencies
    """

    USD = "USD"
    EUR = "EUR"


class Money:
    """
    General Money Class
    """

    def __init__(self, amount: float, currency: Currency) -> None:
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        """
        property to return private instance of amount
        """
        return round(self.__amount, 2)  # pylint: disable=invalid-name

    @amount.setter
    def amount(self, value: float) -> None:
        """
        property setter for ensuring correct setting of private instance of amount
        """
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"Invalid Amount ({value})")
        self.__amount = value  # pylint: disable=invalid-name

    def __repr__(self):
        return f'{self.currency}({{"ID": {id(self)}, "amount": {self.amount}}})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        logger.debug("self=%s", self.amount)
        logger.debug("other=%s", other.amount)
        cur = self.currency == other.currency
        amount = self.amount == other.amount
        return cur and amount

    def __mul__(self, other: Money) -> Money:
        # get Current Currency Rates
        exchange = round(converter.get_rate(other.currency.value, self.currency.value), 2)
        multipland = other.amount * exchange
        return Money(self.amount * multipland, self.currency)

    def __add__(self, other: Money) -> Money:
        # get Current Currency Rates
        exchange = round(converter.get_rate(other.currency.value, self.currency.value), 2)
        addipland = other.amount * exchange
        return Money(self.amount + addipland, self.currency)
