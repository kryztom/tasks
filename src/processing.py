from datetime import datetime


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению"""

    if not list_of_dict:
        raise ValueError("Список транзакций пуст")

    filtered_list = [dict_item for dict_item in list_of_dict if dict_item.get("state") == state]

    if not filtered_list:
        raise ValueError("Ни одной транзакции с данным состоянием не найдено")

    return filtered_list


def sort_by_date(data_list: list, descending: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
     новый список, отсортированный по дате (date)."""
    if not data_list:
        raise ValueError("Список транзакций пуст")

    for item in data_list:
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError("Некорректный формат даты")

    return sorted(data_list, key=lambda x: x["date"], reverse=descending)

    # Проверка работы кода


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )

    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
