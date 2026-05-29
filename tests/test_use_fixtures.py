import pytest

@pytest.fixture
def clear_database()->None:
    print("\nclearing database\n--------------")
@pytest.fixture
def fill_database()->None:
    print("\ncreating new data for database\n--------------")

@pytest.mark.usefixtures("clear_database", "fill_database")
def test_read_all_books_in_library():
    print("\ntesting read_all_books_in_library\n--------------")

@pytest.mark.usefixtures(
    "clear_database",
    "fill_database"
)
class TestLibrary:
    def test_read_books_from_library(self):
        ...
    def test_delete_books_from_library(self):
        ...