from datetime import date
from typing import Protocol
from pay.order import Order
import pytest
from pay.credit_card import CreditCard


class PaymentProcessor(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int):
        """Charges the card with the amount. Doesn't change anything int he rest of the code"""


def pay_order(order: Order, card: CreditCard, processor: PaymentProcessor):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")

    processor.charge(card, amount=order.total)
    order.pay()
