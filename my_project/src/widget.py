from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    '''Функция, которая обрабатывет информацию как о картах,
    так и о счетах '''
    account_card_list = []
    account_card_split = account_card.split()

    for word in account_card_split:
        if word.isalpha():
            account_card_list.append(word)
    card_type = ''.join(account_card_list)

    number_card = account_card_split[-1]
    if account_card_split[0].lower() == "счет":

        return f'{card_type} {get_mask_account(number_card)}'
    else:

        return f'{card_type} {get_mask_card_number(number_card)}'


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
        'Maestro 1596837868705199',
        'Счет 64686473678894779589',
        'MasterCard 7158300734726758',
        'Счет 35383033474447895560',
        'Visa Classic 6831982476737658',
        'Visa Platinum 8990922113665229',
        'Visa Gold 5999414228426353',
        'Счет 73654108430135874305'
    ]:
        print(mask_account_card(data))



