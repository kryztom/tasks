import pytest

from src.widget import mask_account_card, get_date

"""Делаем проверку функции mask_account_card """


@pytest.mark.parametrize('account_card , expected', [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "VisaClassic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "VisaPlatinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "VisaGold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


"""Проверка если номер  больше 30 цифр"""


def test_mask_account_card_big():
    with pytest.raises(ValueError):
        mask_account_card("126368966922533535353523232335")


"""Проверка если номер пустой"""


def test_mask_account_card_empty():
    with pytest.raises(ValueError):
        mask_account_card(" ")


"""Проверка если номер меньше 16 цифр"""


def test_mask_account_card_little():
    with pytest.raises(ValueError):
        mask_account_card("126")


"""Делаем проверку функции get_date """


@pytest.mark.parametrize('date, expected',
                         [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date, expected):
    assert get_date(date) == expected


"""Проверяем если дата пустая"""


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")


"""Проверяем если дата меньше 10 цифр"""


def test_get_date_little():
    with pytest.raises(ValueError):
        get_date("3789-29")


"""Проверяем если дата больше 30 цифр """


def test_get_date_big():
    with pytest.raises(ValueError):
        get_date("2952598-25295809ujf220-f24844482883345353535")
