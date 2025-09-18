import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.usefixtures("sample_transactions")
def test_filter_by_currency_another_currency(sample_transactions):
    # Тест фильтрации по несуществующей валюте
    eur_transactions = list(filter_by_currency(sample_transactions, ""))

    assert len(eur_transactions) == 0
    assert eur_transactions == []


def test_filter_by_currency(sample_transactions):
    assert list(filter_by_currency(sample_transactions, "USD")) == [
        {
            "id": 1,
            "description": "Transaction in USD",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 3,
            "description": "Another USD transaction",
            "operationAmount": {
                "amount": "150",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


# Фикстура с примером транзакций
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Transaction in USD",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 2,
            "description": "Transaction in EUR",
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "EUR", "code": "EUR"}
            }
        },
        {
            "id": 3,
            "description": "Another USD transaction",
            "operationAmount": {
                "amount": "150",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


# Параметризация для теста фильтрации по валюте
@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [1, 3, 939719570]),
    ("EUR", [2]),
    ("RUB", [])
])
def test_filter_by_currency_with_parametrize(sample_transactions, currency_code, expected_ids):
    result = list(filter_by_currency(sample_transactions, currency_code))
    result_ids = [tx["id"] for tx in result]
    assert result_ids == expected_ids


# Тест для функции описаний транзакций
def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Transaction in USD",
        "Transaction in EUR",
        "Another USD transaction",
        "Перевод организации"
    ]
    assert descriptions == expected_descriptions


# Параметризация для генератора номеров карт
@pytest.mark.parametrize("start, end, expected_numbers", [
    (
        1,
        3,
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]
    ),
    (
        9999999999999998,
        9999999999999999,
        [
            "9999 9999 9999 9998",
            "9999 9999 9999 9999"
        ]
    )
])
def test_card_number_generator(start, end, expected_numbers):
    gen = card_number_generator(start, end)
    generated_numbers = list(gen)
    assert generated_numbers == expected_numbers


# Тест для проверки формата номера карты
def test_card_number_format():
    gen = card_number_generator(1, 1)
    card_number = next(gen)
    # Проверка, что номер состоит из 4 групп по 4 цифры
    parts = card_number.split()
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()
