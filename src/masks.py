def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде
         числа и возвращает маску номера по правилу
         XXXX XX** **** XXXX
    ."""
    card_number = str(card_number)
    if len(card_number) < 16 or len(card_number) > 16:
        raise ValueError("Неверный номер карты")

    elif len(card_number) == 16:
        mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

        return mask_number


def get_mask_account(account_number: int) -> str:
    """Функция
     принимает на вход номер счета в виде числа и
     возвращает маску номера по правилу **XXXX
    ."""
    account_number = str(account_number)
    if len(account_number) < 4 or len(account_number) > 20:
        raise ValueError("Неверный номер карты")

    if len(account_number) >= 4:
        mask_account = f"**{account_number[-4:]}"
        return mask_account


# Проверка работы кода
if __name__ == "__main__":
    print(get_mask_account(90123456))

    print(get_mask_card_number(1234567890123456))
