import pytest
from main import BooksCollector  # предполагая, что ваш класс находится в файле main.py


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    #Description: Проверка add_new_book
    def test_add_new_book(self, collector):
        collector.add_new_book("Book_1")
        assert "Book_1" in collector.get_books_genre()

    #Description: Проверка add_new_book, книга с именем длиной 41 символ, проверка граничного значения
    def test_add_new_book_too_long(self, collector):
        collector.add_new_book("A" * 41)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize("name, genre", [
        ("Book_1", "Фантастика"),
        ("Book_2", "Ужасы"),
    ])

    #Description: Проверка get_book_genre.
    def test_set_book_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    #Description: Проверка get_book_genre.
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Book_1")
        collector.add_new_book("Book_2")
        collector.set_book_genre("Book_1", "Фантастика")
        collector.set_book_genre("Book_2", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Book_1"]
        assert collector.get_books_with_specific_genre("Ужасы") == ["Book_2"]

    # Description: Проверка get_books_with_specific_genre
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Book_1")
        collector.add_new_book("Book_2")
        collector.set_book_genre("Book_1", "Фантастика")
        collector.set_book_genre("Book_2", "Ужасы")
        child_friendly_books = collector.get_books_for_children()
        assert "Book_1" in child_friendly_books
        assert "Book_2" not in child_friendly_books

    # Description: Проверка get_books_for_children
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Book_1")
        collector.add_book_in_favorites("Book_1")
        assert "Book_1" in collector.get_list_of_favorites_books()

    # Description: Проверка add_book_in_favorites
    def test_add_book_in_favorites_not_exist(self, collector):
        collector.add_book_in_favorites("Book_1")
        assert "Book_1" not in collector.get_list_of_favorites_books()

    # Description: Проверка delete_book_from_favorites
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Book_1")
        collector.add_book_in_favorites("Book_1")
        collector.delete_book_from_favorites("Book_1")
        assert "Book_1" not in collector.get_list_of_favorites_books()

    # Description: Проверка get_list_of_favorites_books
    def test_delete_book_from_favorites_not_exist(self, collector):
        collector.add_new_book("Book_1")
        collector.delete_book_from_favorites("Book_1")
        assert "Book_1" not in collector.get_list_of_favorites_books()
