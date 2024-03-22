import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre.keys()) == 2

    def test_set_book_genre_set_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Зловещие мертвецы 2')
        collector.set_book_genre('Зловещие мертвецы 2', 'Ужасы')

        assert collector.books_genre['Зловещие мертвецы 2'] == 'Ужасы'

    def test_get_book_genre_get_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_true(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        collector.add_new_book('Зловещие мертвецы 2')
        collector.set_book_genre('Зловещие мертвецы 2', 'Ужасы')

        assert 'Зловещие мертвецы 2' in collector.get_books_with_specific_genre('Ужасы') and 'Гордость и предубеждение и зомби' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_genre_curent_status(self, list_book):
        for i in list_book.books_genre.keys():
            assert i in list_book.books_genre

    def test_get_books_for_children_true(self, books_for_children):
        assert 'Зловещие мертвецы 2' not in books_for_children.get_books_for_children()

    def test_add_book_in_favorites_add_one(self):
        collector = BooksCollector()

        collector.add_new_book('Джей и молчаливый Боб')
        collector.add_book_in_favorites('Джей и молчаливый Боб')

        assert 'Джей и молчаливый Боб' in collector.books_genre and collector.favorites

    @pytest.mark.parametrize('favorites', ['Очень страшное кино'])
    def test_delete_book_from_favorites_delete_one_book(self, favorites):
        collector = BooksCollector()

        collector.add_new_book(favorites)
        collector.add_book_in_favorites(favorites)
        collector.delete_book_from_favorites(favorites)
        assert collector.favorites == []

    def test_get_list_of_favorites_books_true(self, favorit_book):
        collector = BooksCollector()

        collector.add_new_book('Джей и молчаливый Боб')
        collector.add_book_in_favorites('Джей и молчаливый Боб')

        collector.add_new_book('Очень страшное кино')
        collector.add_book_in_favorites('Очень страшное кино')
        assert collector.get_list_of_favorites_books() == favorit_book

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()