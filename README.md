# Создаем учебный проект для банковских продуктов

## Описание

создаем учебный проект по заданиям на языке Python для банковских продуктов

## Описание

Создаем папку тест где тестируем все функции для банковского проета .

### Установка

		1. Убедись, что у тебя установлен Python версии >=3.13.


		2. Склонируй репозиторий:

'''
git clone https://github.com/username/repository.git
'''

		3. Установи зависимости:

'''
pip install -r requirements.txt
'''

        4. Установка pytest

'''
poetry add --group dev pytest
'''

        5. Установка Code coverage

'''
poetry add --group dev pytest-cov
'''

## Использование

Пример использования функций:

from src.processing import filter_by_state, sort_by_date

operations = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]

# Фильтрация по статусу

executed_ops = filter_by_state(operations)

# Сортировка по дате

sorted_ops = sort_by_date(operations)

### Версии для данного проекта

requires-python = ">=3.13"
flake8 = "^7.3.0"
black = "^25.1.0"
isort = "^6.0.1"
mypy = "^1.16.1"
pytest = ">=6.2.5"
