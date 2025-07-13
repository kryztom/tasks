def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:


    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению"""
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get('state') == state:
            filtered_list.append(dict_item)

    return filtered_list


