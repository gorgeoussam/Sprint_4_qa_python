import pytest


from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books_true(self):

        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize(
                            'name, genre',
                            [
                            ['Гордость и предубеждение и зомби', 'Фантастика'],
                            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
                            ['The Hitchhikers Guide to the Galaxy', 'Мультфильмы']
                            ]
                        )
    def test_set_book_genre_assigns_genre_true(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == genre



    def test_get_book_genre_returns_correct_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        result = collector.get_book_genre('Гордость и предубеждение и зомби')
        expected = 'Фантастика'
        assert result == expected

    def test_get_books_with_specific_genre_returns_correct_genre_true(self, books_collector):
        result = books_collector.get_books_with_specific_genre('Фантастика')
        expected = ['Гордость и предубеждение и зомби', 'The Hitchhikers Guide to the Galaxy']
        assert result == expected

    def test_get_books_genre_returns_books_genre_dictionary_true(self, books_collector):
        result = books_collector.get_books_genre()
        expected = {
            'Гордость и предубеждение и зомби': 'Фантастика',
            'The Hitchhikers Guide to the Galaxy': 'Фантастика',
            'Что делать, если ваш кот хочет вас убить': 'Ужасы'
        }
        assert result == expected

    def test_get_books_for_children_returns_not_genre_age_rating_true(self, books_collector):
        result = books_collector.get_books_for_children()
        expected = ['Гордость и предубеждение и зомби', 'The Hitchhikers Guide to the Galaxy']
        assert result == expected


    def test_add_book_in_favorites_add_one_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

    def test_delete_book_from_favorites_delete_book_empty_list_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_returns_list_of_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

