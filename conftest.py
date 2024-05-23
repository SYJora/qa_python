import pytest
from main import BooksCollector


@pytest.fixture
def list_book():
    collector = BooksCollector()

    collector.add_new_book('Зловещие мертвецы 2')
    collector.add_new_book('Зловещие мертвецы 3')
    collector.add_new_book('Зловещие мертвецы 4')
    collector.add_new_book('Зловещие мертвецы 5')
    return collector

@pytest.fixture
def books_for_children():
    collector = BooksCollector()

    collector.add_new_book('Тайна Коко')
    collector.set_book_genre('Тайна Коко', 'Мультфильмы')

    collector.add_new_book('Зловещие мертвецы 2')
    collector.set_book_genre('Зловещие мертвецы 2', 'Ужасы')

    collector.add_new_book('Убийство в Восточном экспрессе')
    collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')

    return collector


@pytest.fixture
def favorit_book():
    return ['Джей и молчаливый Боб', 'Очень страшное кино']