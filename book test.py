import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedżmin", "Sapkowski", 2000)
    def test_get_info(self):
        text_correct = "Książka: Wiedżmin Aurhor: Sapkowski Rok: 2000"
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)

    def test_change_title(self):
        self.book.change_title("Miecz przeznaczenia")
        self.assertEqual("Miecz przeznaczenia", self.book.title)

    def test_change_author(self):
        self.book.change_author("Sapkowski2")
        self.assertEqual("Sapkowski2", self.book.author)

    def test_change_year(self):
        self.book.change_year(2001)
        self.assertEqual(2001, self.book.year)

if __name__ == '__main__':
    unittest.main()
