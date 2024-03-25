import pytest
from main import BooksCollector

@pytest.fixture(scope='class')
def collector_list():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.add_new_book('Бэмби')
    collector.add_new_book('Дюна')
    collector.add_new_book('1984')
    collector.add_new_book('451 градус по Фаренгейту')
    return collector