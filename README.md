# qa_python

### Tests description:

## 1. def test_add_new_book_add_two_books_true
checks **add_new_book** adds books to collector.books_genre by checking it's length

## 2. test_set_book_genre_assigns_genre_true
checks assigned genre is returned from the dictionary books_genre by name

## 3. test_get_book_genre_returns_correct_genre_true
creates a book and assigns it a genre with collector.set_book_genre
checks correct genre is returned with get_book_genre

## 4. test_get_books_with_specific_genre_returns_correct_genre_true
books_collector() fixture has 3 books added, two of them are same genre 'Фантастика'
test checks get_books_with_specific_genre('Фантастика') returns only books with 'Фантастика' genre:
[Гордость и предубеждение и зомби,'The Hitchhikers Guide to the Galaxy']

## 5. test_get_books_genre_returns_books_genre_dictionary_true
tests dictionary books_genre is returned for books_collector with three books added

## 6. test_get_books_for_children_returns_not_genre_age_rating_true
three books are added to books_collector, test checks 'Фантастика' genre is returned and 'Ужасы' is not

## 7. test_add_book_in_favorites_add_one_book_true
checks book name is in favorite list after adding

## 8. test_delete_book_from_favorites_delete_book_empty_list
checks favorites list is empty after book is added and deleted

## 9. test_get_list_of_favorites_returns_list_of_favorites_true
adding a book to favorites list, checking list with book name is returned

