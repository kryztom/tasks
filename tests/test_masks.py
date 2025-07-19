import pytest

from src.masks import get_mask_card_number, get_mask_account

"""Делаем проверку функции get_mask_card_number """


@pytest.mark.parametrize('card_number, expected', [
    ("1234567890123456", "1234 56** **** 3456")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


"""Проверка если номер карты меньше 16 цифр"""


def test_get_mask_card_number_litle():
    with pytest.raises(ValueError):
        get_mask_card_number("1263689669")


"""Проверка если номер карты больше 16 цифр"""


def test_get_mask_card_number_big():
    with pytest.raises(ValueError):
        get_mask_card_number("126368966922533535353535")


"""Проверка если номер карты меньше 0 цифр"""


def test_get_mask_card_number_zero():
    with pytest.raises(ValueError):
        get_mask_card_number(" ")


"""Делаем проверку функции get_get_mask_account """


@pytest.mark.parametrize('mask_account, expected', [
    ("123456", "**3456")
])
def test_get_mask_account(mask_account, expected):
    assert get_mask_account(mask_account) == expected


"""Проверка если номер счета меньше 4 цифр"""


def test_get_mask_account_litle():
    with pytest.raises(ValueError):
        get_mask_account("123")


"""Проверка если номер счета больше 20 цифр"""


def test_get_mask_account_big():
    with pytest.raises(ValueError):
        get_mask_account("126368966922533535353523232335")


"""Проверка если номер счета 0 цифр"""


def test_get_mask_account_zero():
    with pytest.raises(ValueError):
        get_mask_account(" ")
