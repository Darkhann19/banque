import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return "7000792289606361"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_wrong():
    assert get_mask_card_number("112") == "Неправильный номер карты"


@pytest.mark.parametrize("number, mask_number", [
    ("112233", "**2233"),
    ("11111111111111", "**1111"),
    ("22343995400", "**5400")
])
def test_get_mask_account(number, mask_number):
    assert get_mask_account(number) == mask_number


def test_get_mask_account_wrong():
    assert get_mask_account("324") == "Неправильный номер счета"