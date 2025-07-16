import pytest

from my_project.src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_number, expected', [
    ("1234567890123456", "1234 56 ** **** 3456")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_litle():
    with pytest.raises(ValueError):
        get_mask_card_number("1263689669")

def test_get_mask_card_number_big():
    with pytest.raises(ValueError):
        get_mask_card_number("126368966922533535353535")

def test_get_mask_card_number_zero():
    with pytest.raises(ValueError):
        get_mask_card_number(" ")



@pytest.mark.parametrize('mask_account, expected', [
    ("123456", "**3456")
])
def test_get_mask_account(mask_account, expected):
    assert get_mask_account(mask_account) == expected


def test_get_mask_account_litle():
    with pytest.raises(ValueError):
        get_mask_account("123")

def test_get_mask_account_big():
    with pytest.raises(ValueError):
        get_mask_account("126368966922533535353535")

def test_get_mask_account_zero():
    with pytest.raises(ValueError):
        get_mask_account(" ")