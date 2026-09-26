import unittest
from unittest.mock import patch

from app import Figure, count_vowels, read_positive_number, validate_positive_number


class TestNumberValidation(unittest.TestCase):
    def test_correct_number(self):
        self.assertEqual(8, validate_positive_number(8))

    def test_incorrect_number(self):
        with self.assertRaisesRegex(ValueError, "більшим за нуль"):
            validate_positive_number(-3)

    def test_not_a_number(self):
        with self.assertRaisesRegex(ValueError, "Потрібно ввести число"):
            validate_positive_number("вісім")


class TestCountVowels(unittest.TestCase):
    def test_english_text(self):
        self.assertEqual(4, count_vowels("Testing Python"))

    def test_text_without_vowels(self):
        self.assertEqual(0, count_vowels("bcdfg"))

    def test_uppercase_letters(self):
        self.assertEqual(5, count_vowels("AEIOU"))

    def test_empty_string(self):
        self.assertEqual(0, count_vowels(""))

    def test_string_with_digits(self):
        self.assertEqual(0, count_vowels("1234567890"))

    def test_ukrainian_letters(self):
        self.assertEqual(6, count_vowels("Українське слово"))


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_all_figure_types_with_subtest(self):
        expected_angles = {
            "квадрат": 4,
            "прямокутник": 4,
            "трикутник": 3,
        }

        for figure_type, angles in expected_angles.items():
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 2)
                self.assertEqual(figure_type, figure.get_figure_type)
                self.assertEqual(angles, figure.get_angles)

    def test_zero_length(self):
        with self.assertRaisesRegex(AssertionError, "більшою за 0"):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaisesRegex(AssertionError, "більшою за 0"):
            Figure("трикутник", -2)

    def test_unknown_figure(self):
        with self.assertRaisesRegex(AssertionError, "Невідомий тип"):
            Figure("коло", 1)


class TestInputWithMock(unittest.TestCase):
    @patch("builtins.input", return_value="7")
    def test_read_positive_number(self, mock_input):
        self.assertEqual(7, read_positive_number())
        mock_input.assert_called_once_with("Введіть додатне ціле число: ")

    @patch("builtins.input", return_value="-1")
    def test_read_incorrect_number(self, mock_input):
        with self.assertRaises(ValueError):
            read_positive_number()
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
