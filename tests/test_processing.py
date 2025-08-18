import pytest

from src.processing import filter_by_state, sort_by_date

""" Проверка работы функции filter_by_state """


@pytest.mark.parametrize('list_of_dict, state, expected', [
    (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
            ]
    ),
    (
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
            ]
    )
])
def test_filter_by_state(list_of_dict: list, state: str, expected: list) -> None:
    assert filter_by_state(list_of_dict, state) == expected


"""Проверка если список будет пуст """


def test_filter_by_empty() -> None:
    with pytest.raises(ValueError):
        filter_by_state([])


"""Проверка если state пуст"""


def test_filter_by_state_empty() -> None:
    with pytest.raises(ValueError):
        filter_by_state(["65830300398"], " ")


"""Проверка если state = CANCE"""


def test_filter_by_state_not_correct() -> None:
    with pytest.raises(ValueError):
        filter_by_state(["3693469396"], "CANCE")


"""Проверка функции sort_by_date"""


@pytest.mark.parametrize('data_list, descending, expected', [
    (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
            ],
            True,
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
            ]
    )
])
def test_sort_by_date(data_list: list, descending: bool, expected: list) -> None:
    assert sort_by_date(data_list, descending) == expected


"""Тестирование сортировки списка словарей по датам в порядке возрастания"""


def test_sort_by_date_false() -> None:
    with pytest.raises(ValueError):
        sort_by_date({'id': 41428827, 'state': 'EXECUTED', 'date': '2016-07-03T18:35:29.512364'},
                     False)


"""Проверка корректности сортировки при одинаковых датах."""


def test_sort_by_date_date() -> None:
    with pytest.raises(ValueError):
        sort_by_date([
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
        ], True)


"""Тесты на работу функции с некорректными или нестандартными форматами дат"""


def test_sort_by_date_little() -> None:
    with pytest.raises(ValueError):
        sort_by_date([
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03'},
        ], True)
