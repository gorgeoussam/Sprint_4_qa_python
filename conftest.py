import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    books_collector = BooksCollector()
    books_collector.add_new_book('Гордость и предубеждение и зомби')
    books_collector.add_new_book('The Hitchhikers Guide to the Galaxy')
    books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    books_collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    books_collector.set_book_genre('The Hitchhikers Guide to the Galaxy', 'Фантастика')
    books_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

    return books_collector