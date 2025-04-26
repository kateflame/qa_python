Необходимо было покрыть методами класс BooksCollector

для этого использовала тесты:
 test_add_new_book_success тест проверяет успешное добавление книг
 test_cannot_add_book_twice тест что нельзя добавить 1 книгу дважды
 test_add_new_book_with_long_name тест для проверки  добавления книг с разными условиями (пустой список, длинные имена, и т.д.)
 test_add_genre_for_book_success тест проверяет что жанр книге добавляется успешно
 test_add_new_book_success_have_empty_genre тест проверяет что у добавленной книги нет жанра
 test_not_exist_genre тест на проверку несуществующего жанра
 test_get_books_with_specific_genre тест на проверку получения книг по жанру
 test_get_books_with_different_genre тест на получение добавления книг с разными жанрами
 test_add_book_in_favorites_success тест проверяет что можно книгу добавить в избранное
 test_delete_book_from_favorites_success тест на удаление книги из избранного
 test_get_not_empty_list_of_favorites_books_success тест на получение списка избранных книг
 test_get_books_for_children тест на книги для детей
 test_get_books_not_for_children негативный тест на книги для детей