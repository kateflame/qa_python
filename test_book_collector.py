import pytest

from data import book_names, long_name_of_books, genres


class TestBooksCollector:

    # добавляем книгу
    def test_add_new_book_success(self, collector):
        collector.add_new_book(book_names[0])
        assert book_names[0] in collector.get_books_genre()

    # нельзя добавить одну книгу дважды
    # добавляем Анну каренину еще раз и проверяем, что длина books_genre не равна 2
    def test_cannot_add_book_twice(self, collector):
        collector.add_new_book(book_names[0])
        collector.add_new_book(book_names[0])
        assert len(collector.get_books_genre()) == 1

    # проверка добавления книг с разными условиями (пустой список, длинные имена, и т.д.)
    @pytest.mark.parametrize(
        "list_of_books, result", [([], 0), (book_names, 3), (long_name_of_books, 0)]
    )
    def test_add_new_book_with_long_name(self, collector, list_of_books, result):
        for book in list_of_books:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == result

    # проверяем установленныый  жанр книги
    def test_add_genre_for_book_success(self, collector):
        collector.add_new_book(book_names[0])
        collector.set_book_genre(book_names[0], genres[0])
        assert collector.get_book_genre(book_names[0]) == genres[0]

    # проверяем что книгу, которую добавили у нее пустой жанр
    def test_add_new_book_success_have_empty_genre(self, collector):
        collector.add_new_book(book_names[0])
        assert collector.get_book_genre(book_names[0]) == ""

    # тест на проверку несуществующего жанра
    def test_not_exist_genre(self, collector):
        collector.add_new_book(book_names[2])
        collector.set_book_genre(book_names[2], "Роутрип")
        assert collector.get_book_genre(book_names[2]) == ""

    # Тест получения книг по жанру
    def test_get_books_with_specific_genre(self, collector_with_books):
        collector_with_books.set_book_genre(book_names[0], genres[0])
        assert book_names[0] in collector_with_books.get_books_with_specific_genre(
            genres[0]
        )

    # Тест на получение добавления книг с разными жанрами
    def test_get_books_with_different_genre(self, collector_with_books):
        collector_with_books.set_book_genre(book_names[0], genres[1])
        collector_with_books.set_book_genre(book_names[1], genres[0])
        assert book_names[0] in collector_with_books.get_books_with_specific_genre(
            genres[1]
        ) and book_names[1] in collector_with_books.get_books_with_specific_genre(
            genres[0]
        )

    # тест на добавляение книг в избранное
    def test_add_book_in_favorites_success(self, collector_with_books):
        collector_with_books.add_book_in_favorites(book_names[1])
        assert book_names[1] in collector_with_books.get_list_of_favorites_books()

    # тест на  удаление книг из избранного
    def test_delete_book_from_favorites_success(self, collector_with_books):
        collector_with_books.add_book_in_favorites(book_names[2])
        collector_with_books.delete_book_from_favorites(book_names[2])
        assert book_names[2] not in collector_with_books.get_list_of_favorites_books()

    # тест на получение списка избранных книг
    def test_get_not_empty_list_of_favorites_books_success(self, collector_with_books):
        collector_with_books.add_book_in_favorites(book_names[2])
        collector_with_books.add_book_in_favorites(book_names[1])
        favorites = collector_with_books.get_list_of_favorites_books()
        assert len(favorites) == 2

    # тест на книги для детей
    def test_get_books_for_children(self, collector_with_books):
        collector_with_books.set_book_genre(book_names[2], genres[3])
        children_books = collector_with_books.get_books_for_children()
        assert book_names[2] in children_books

    # негативный тест на книги для детей
    def test_get_books_not_for_children(self, collector_with_books):
        collector_with_books.set_book_genre(book_names[2], genres[1])
        children_books = collector_with_books.get_books_for_children()
        assert book_names[2] not in children_books
