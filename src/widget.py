from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая обрабатывет информацию как о картах,
    так и о счетах"""
    account_card_list = []
    account_card_split = account_card.split()

    if len(account_card) < 10 or len(account_card) > 30:
        raise ValueError("Неверный номер ")

    for word in account_card_split:
        if word.isalpha():
            account_card_list.append(word)
    card_type = "".join(account_card_list)

    card_number = account_card_split[-1]
    if account_card_split[0].lower() == "счет":

        return f"{card_type} {get_mask_account(card_number)}"
    else:

        return f"{card_type} {get_mask_card_number(card_number)}"


# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305

# Проверка работы кода
if __name__ == "__main__":
    for data in [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]:
        print(mask_account_card(data))


def get_date(date: str) -> str:
    """Функция редактирования даты"""

    if not date or len(date) < 10 or len(date) >30:
        raise ValueError("Неверный формат ")
    date_split = date.split("-")
    date_day = date_split[2][:2]
    date_mouth = date_split[:2]
    date_reverse = ".".join(date_mouth[::-1])
    new_date = f"{date_day}.{date_reverse}"

    return new_date


# Проверка функции
if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
