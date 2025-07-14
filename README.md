# Создаем учебный проект для банковских продуктов

## Описание 
создаем учебный проект по заданиям на языке Python для банковских продуктов


#  Создаем Функцию filter_by_state
которая возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению
## Использование 
'''
filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get('state') == state:
            filtered_list.append(dict_item)

    return filtered_list
    '''
# Создаем функцию sort_by_date
 Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
     новый список, отсортированный по дате
## Использование     
'''
def sort_by_date(data_list: list, data_key, descending=True) -> list:
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], '%Y-%m-%dT%H:%M:%S.%f'), reverse=descending)
    '''
    
