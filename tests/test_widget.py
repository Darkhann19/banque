import pytest
from src.widget import get_date, mask_account_card


@pytest.fixture
def account_card():
    return ["Visa Platinum 7000792289606361", "Счет 73654108430135874305"]


def test_mask_account_card_card(account_card):
    assert mask_account_card(account_card[0]) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account(account_card):
    assert mask_account_card(account_card[1]) == "Счет **4305"


@pytest.mark.parametrize(
    "number, mask_number", [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("American Express 123456789012345", "American Express 1234 56** **** 345"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 11112222333344445555", "Счет **5555"),
        ("Счет 55556666777788889999", "Счет **9999"),
    ])
def test_mask_account_card(number, mask_number):
    assert mask_account_card(number) == mask_number


@pytest.fixture
def incorrect_number():
    return ["", "Счет 123"]


def test_mask_account_card_wrong1(incorrect_number):
    assert mask_account_card(incorrect_number[0]) == "Неправильный номер"


def test_mask_account_card_wrong2(incorrect_number):
    assert mask_account_card(incorrect_number[1]) == "Неправильный номер"


@pytest.fixture
def date_format():
    return "2024-03-11T02:26:18.671407"


def test_get_date(date_format):
    assert get_date(date_format) == "11.03.2024"


def test_get_date_empty():
    assert get_date("") == "Неправильная дата"