from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_bambi_cartoon_true(self,collector_list):
        collector_list.set_book_genre('Бэмби','Мультфильмы')
        assert collector_list.books_genre['Бэмби'] == 'Мультфильмы'

    def test_get_book_genre_bambi_cartoon_true(self,collector_list):
        assert collector_list.get_book_genre('Бэмби') == 'Мультфильмы'

    def test_genre_age_rating_true(self,collector_list):
        # создаем экземпляр (объект) класса BooksCollector
        assert collector_list.genre_age_rating == ['Ужасы', 'Детективы']
    def test_get_books_with_specific_genre_show_fantasy_genre(self,collector_list):
        collector_list.set_book_genre('1984','Фантастика')
        assert collector_list.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_get_books_for_children_true(self,collector_list):
        assert collector_list.get_books_for_children() == ['Бэмби', '1984']

    def test_add_book_in_favorites_add_bambi_shows_bambi(self,collector_list):
        collector_list.add_book_in_favorites('Бэмби')
        assert collector_list.get_list_of_favorites_books() == ['Бэмби']


    def test_delete_book_from_favorites_bambi_shows_empty_list(self,collector_list):
        collector_list.delete_book_from_favorites('Бэмби')
        assert collector_list.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_two_books_shows_two_of_favorites_books(self,collector_list):
        collector_list.add_book_in_favorites('Бэмби')
        collector_list.add_book_in_favorites('451 градус по Фаренгейту')
        assert collector_list.get_list_of_favorites_books() == ['Бэмби','451 градус по Фаренгейту']










