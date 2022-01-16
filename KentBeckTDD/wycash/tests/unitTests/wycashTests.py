import logging
import sys

import pytest

from multiCurrency.currency import (
    Currency,
    Money,
)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

@pytest.mark.parametrize(
    "amount, expected, currency",
    [
        (5, 5, Currency.USD),
        (6, 6, Currency.USD),
        (10.0, 10.0, Currency.USD)
    ]
)
def instantiateMoneyUSDTest(amount, expected, currency):
    a = Money(amount, currency)
    logger.info("a=%s", a)
    assert isinstance(a, Money)
    assert a.amount == expected
    assert a.currency == Currency.USD

@pytest.mark.parametrize(
    "amount, expected, currency",
    [
        (5, 5, Currency.EUR),
        (6, 6, Currency.EUR),
        (10.0, 10.0, Currency.EUR)
    ]
)
def instantiateMoneyEURTest(amount, expected, currency):
    a = Money(amount, currency)
    logger.info("a=%s", a)
    assert isinstance(a, Money)
    assert a.amount == expected
    assert a.currency == Currency.EUR

@pytest.mark.parametrize(
    "amount",
    [
        -3,
        "foo",
        {"foo": "bar"},
        [1,2]
    ]
)
def instantiateMoneyValueErrorTest(amount):
    with pytest.raises(ValueError) as error:
        Money(amount, Currency.USD)
    logger.info("Value Error Correctly raised error=%s", error.value)

@pytest.mark.parametrize(
    "a, b",
    [
        (Money(5, Currency.USD), Money(5, Currency.USD)),
        (Money(10.0123, Currency.EUR), Money(10.0123, Currency.EUR))
    ]
)
def equalCurrencyTest(a, b):
    assert a == b

@pytest.mark.parametrize(
    "a, b",
    [
        (Money(5, Currency.USD), Money(5, Currency.EUR)),
        (Money(10.0, Currency.EUR), Money(10.0, Currency.USD))
    ]
)
def notEqualDifferntCurrencyTest(a, b):
    assert a != b

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Money(5, Currency.USD), Money(2, Currency.USD), Money(10, Currency.USD)),
        (Money(5, Currency.USD), Money(2, Currency.EUR), Money(8.74, Currency.USD)),
        (Money(5, Currency.EUR), Money(2, Currency.USD), Money(11.45, Currency.EUR))
    ]
)
def multiplyCurrenciesWithCurrencyRatesTest(a, b, expected):
    logger.info("%s * %s == %s", a, b, expected)
    assert a * b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Money(5, Currency.USD), Money(2, Currency.USD), Money(7, Currency.USD)),
        (Money(5, Currency.USD), Money(2, Currency.EUR), Money(7.28, Currency.USD)),
        (Money(5, Currency.EUR), Money(2, Currency.USD), Money(6.74, Currency.EUR))
    ]
)
def addCurrenciesWithCurrencyRatesTest(a, b, expected):
    logger.info("%s * %s == %s", a, b, expected)
    assert a + b == expected
