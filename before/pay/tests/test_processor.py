from datetime import date
import pytest
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""

CC_YEAR = date.today().year + 2


@pytest.fixture
def payment_processor() -> PaymentProcessor:
    return PaymentProcessor(API_KEY)


def test_api_key_invalid() -> None:
    with pytest.raises(ValueError):
        card = CreditCard("1249190007575069", 12, CC_YEAR)
        PaymentProcessor("").charge(card, 100)


def test_card_valid_date(payment_processor: PaymentProcessor) -> None:
    card = CreditCard("1249190007575069", 12, CC_YEAR)
    assert payment_processor.validate_card(card)



def test_card_invalid_date(payment_processor: PaymentProcessor) -> None:
    card = CreditCard("1249190007575069", 12, 1900)
    assert not payment_processor.validate_card(card)
