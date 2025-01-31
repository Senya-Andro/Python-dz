import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):

    def setUp(self):
        self.utils = StringUtils()

    # Тесты для функции capitilize
    def test_capitilize(self):
        self.assertEqual(self.utils.capitilize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitilize(""), "")
        self.assertEqual(self.utils.capitilize(" "), " ")
        self.assertEqual(self.utils.capitilize("123"), "123")
        self.assertEqual(self.utils.capitilize("тест"), "Тест")

    # Тесты для функции trim
    def test_trim(self):
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim(""), "")
        self.assertEqual(self.utils.trim(" "), "")
        self.assertEqual(self.utils.trim("  тест  "), "тест  ")

    # Тесты для функции to_list
    def test_to_list(self):
        self.assertEqual(self.utils.to_list("a,b,c,d"), ["a", "b", "c", "d"])
        self.assertEqual(self.utils.to_list("1:2:3", ":"), ["1", "2", "3"])
        self.assertEqual(self.utils.to_list(""), [])
        self.assertEqual(self.utils.to_list(" ", ","), [])  # Ожидается пустой список
        self.assertEqual(self.utils.to_list("тест,пример", ","), ["тест", "пример"])

    # Тесты для функции contains
    def test_contains(self):
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertFalse(self.utils.contains("SkyPro", "U"))
        self.assertFalse(self.utils.contains("", "S"))
        self.assertFalse(self.utils.contains(" ", "S"))
        self.assertTrue(self.utils.contains("тест", "т"))

    # Тесты для функции delete_symbol
    def test_delete_symbol(self):
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "Pro"), "Sky")
        self.assertEqual(self.utils.delete_symbol("", "S"), "")
        self.assertEqual(self.utils.delete_symbol(" ", " "), "")
        self.assertEqual(self.utils.delete_symbol("тест", "т"), "ес")

    # Тесты для функции starts_with
    def test_starts_with(self):
        self.assertTrue(self.utils.starts_with("SkyPro", "S"))
        self.assertFalse(self.utils.starts_with("SkyPro", "P"))
        self.assertFalse(self.utils.starts_with("", "S"))
        self.assertFalse(self.utils.starts_with(" ", "S"))
        self.assertTrue(self.utils.starts_with("тест", "т"))

    # Тесты для функции end_with
    def test_end_with(self):
        self.assertTrue(self.utils.end_with("SkyPro", "o"))
        self.assertFalse(self.utils.end_with("SkyPro", "y"))
        self.assertFalse(self.utils.end_with("", "o"))
        self.assertFalse(self.utils.end_with(" ", "o"))
        self.assertTrue(self.utils.end_with("тест", "т"))

    # Тесты для функции is_empty
    def test_is_empty(self):
        self.assertTrue(self.utils.is_empty(""))
        self.assertTrue(self.utils.is_empty(" "))
        self.assertFalse(self.utils.is_empty("SkyPro"))
        self.assertFalse(self.utils.is_empty("тест"))

    # Тесты для функции list_to_string
    def test_list_to_string(self):
        self.assertEqual(self.utils.list_to_string([1, 2, 3, 4]), "1, 2, 3, 4")
        self.assertEqual(self.utils.list_to_string(["Sky", "Pro"]), "Sky, Pro")
        self.assertEqual(self.utils.list_to_string(["Sky", "Pro"], "-"), "Sky-Pro")
        self.assertEqual(self.utils.list_to_string([]), "")
        self.assertEqual(self.utils.list_to_string(["тест", "пример"], "-"), "тест-пример")

if __name__ == '__main__':
    unittest.main()