import pytest

from checkout import Checkout


class TestCheckout:
    @pytest.fixture
    def checkout(self) -> Checkout:
        checkout = Checkout()
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        yield checkout

    def test_CreateInstanceOfCheckout(self, checkout) -> None:
        assert isinstance(checkout, Checkout)

    def test_CanCalcuateItemTotal(self, checkout) -> None:
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(self, checkout) -> None:
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_CanAddDiscountRule(self, checkout) -> None:
        checkout.addDiscount("a", 3, 2)

    def test_CanApplyDiscountRule(self, checkout) -> None:
        checkout.addDiscount("a", 3, 2)
        checkout.addItem("a")
        checkout.addItem("a")
        checkout.addItem("a")
        assert checkout.calculateTotal() == 2

    def test_ExceptionWithBadItem(checkout) -> None:
        with pytest.raises(Exception):
            checkout.addItem("c")
