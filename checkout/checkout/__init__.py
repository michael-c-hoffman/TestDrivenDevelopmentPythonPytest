"""
Module information
"""
class Checkout:
    class Discount:
        def __init__(self, numItems: int, price: float):
            self.numItems = numItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item: str, price: float) -> None:
        self.prices[item] = price

    def addItem(self, item: str) -> None:
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self) -> float:
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item: str, cnt: int) -> float:
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.numItems:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculateItemDiscountedTotal(self, item: str, cnt: int, discount) -> float:
        total = 0
        numDiscounts = cnt / discount.numItems
        total += numDiscounts * discount.price
        remaining = cnt % discount.numItems
        total += remaining * self.prices[item]
        return total

    def addDiscount(self, item: str, numItems: int, price: float) -> None:
        self.discounts[item] = self.Discount(numItems, price)
