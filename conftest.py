import pytest


from main import BooksCollector
import data


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    collector.add_new_book(data.book_names[0])
    collector.add_new_book(data.book_names[1])
    collector.add_new_book(data.book_names[2])
    return collector
