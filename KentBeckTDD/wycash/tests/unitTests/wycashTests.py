"""
tests for multicurrency
"""
from forex_python import converter
import logging
import sys

import pytest
from multiCurrency.currency import Currency, Money

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


@pytest.mark.parametrize(
    "amount, expected, currency",
    [(5, 5, Currency.USD), (6, 6, Currency.USD), (10.0, 10.0, Currency.USD)],
)
def instantiateMoneyUSDTest(amount, expected, currency):
    """
    test instantiate USD
    """
    first = Money(amount, currency)
    logger.info("a=%s", first)
    assert isinstance(first, Money)
    assert first.amount == expected
    assert first.currency == Currency.USD


@pytest.mark.parametrize(
    "amount, expected, currency",
    [(5, 5, Currency.EUR), (6, 6, Currency.EUR), (10.0, 10.0, Currency.EUR)],
)
def instantiateMoneyEURTest(amount, expected, currency):
    """
    test instantiate EUR
    """
    first = Money(amount, currency)
    logger.info("a=%s", first)
    assert isinstance(first, Money)
    assert first.amount == expected
    assert first.currency == Currency.EUR


@pytest.mark.parametrize("amount", [-3, "foo", {"foo": "bar"}, [1, 2]])
def instantiateMoneyValueErrorTest(amount):
    """
    test with invalid value
    """
    with pytest.raises(ValueError) as error:
        Money(amount, Currency.USD)
    logger.info("Value Error Correctly raised error=%s", error.value)


@pytest.mark.parametrize(
    "first, second",
    [
        (Money(5, Currency.USD), Money(5, Currency.USD)),
        (Money(10.0123, Currency.EUR), Money(10.0123, Currency.EUR)),
    ],
)
def equalCurrencyTest(first, second):
    """
    validate __eq__
    """
    assert first == second


@pytest.mark.parametrize(
    "first, second",
    [
        (Money(5, Currency.USD), Money(5, Currency.EUR)),
        (Money(10.0, Currency.EUR), Money(10.0, Currency.USD)),
    ],
)
def notEqualDifferntCurrencyTest(first, second):
    """
    validate not __eq__
    """
    assert first != second


@pytest.mark.parametrize(
    "first, second",
    [
        (Money(5, Currency.USD), object()),
    ],
)
def notImplementedDifferntCurrencyTest(first, second):
    """
    validate not implemented
    """
    assert first != second


@pytest.mark.parametrize(
    "first, second, expected, exchange",
    [
        (Money(5, Currency.USD), Money(2, Currency.USD), Money(10, Currency.USD), 1),
        (Money(5, Currency.USD), Money(2, Currency.EUR), Money(15, Currency.USD), 1.5),
        (Money(5, Currency.EUR), Money(2, Currency.USD), Money(5, Currency.EUR), 0.5),
    ],
)
def multiplyCurrenciesWithCurrencyRatesTest(monkeypatch, first, second, expected, exchange):
    """
    multiple curencies with currency rates
    """
    def mockExchange(*args, **kwargs):
        logger.debug("MOCKING MOCKEXCHANGE!!!!!!!")
        return exchange
    monkeypatch.setattr(converter, 'get_rate', mockExchange)
    logger.info("%s * %s == %s", first, second, expected)
    assert first * second == expected

@pytest.mark.parametrize(
    "first, second, expected, exchange",
    [
        (Money(5, Currency.USD), Money(2, Currency.USD), Money(7, Currency.USD), 1.0),
        (Money(5, Currency.USD), Money(2, Currency.EUR), Money(9, Currency.USD), 2.0),
        (Money(5, Currency.EUR), Money(2, Currency.USD), Money(6, Currency.EUR), 0.5),
    ],
)
def addCurrenciesWithCurrencyRatesTest(monkeypatch, first, second, expected, exchange):
    """
    add currencies with currency rates
    """
    def mockExchange(*args, **kwargs):
        logger.debug("MOCKING MOCKEXCHANGE!!!!!!!")
        return exchange
    monkeypatch.setattr(converter, 'get_rate', mockExchange)
    logger.info("%s + %s == %s", first, second, expected)
    assert first + second == expected
