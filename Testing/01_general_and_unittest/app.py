class Figure:
    """Геометрична фігура з типом та довжиною сторони."""

    FIGURES = ("квадрат", "прямокутник", "трикутник")
    ANGLES = {
        "квадрат": 4,
        "прямокутник": 4,
        "трикутник": 3,
    }

    def __init__(self, figure_type: str, length: int | float) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.type

    @property
    def get_figure_length(self) -> int | float:
        return self.length

    @property
    def get_angles(self) -> int:
        """Повертає кількість кутів фігури."""
        return self.ANGLES[self.type]


def validate_positive_number(number: int | float) -> int | float:
    """Перевіряє, що значення є додатним числом."""
    if isinstance(number, bool) or not isinstance(number, (int, float)):
        raise ValueError("Потрібно ввести число")
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return number


def count_vowels(text: str) -> int:
    """Рахує англійські та українські голосні літери у рядку."""
    vowels = set("aeiouyаеиіоуяюєї")
    return sum(symbol in vowels for symbol in text.casefold())


def read_positive_number() -> int:
    """Зчитує ціле число за допомогою input() та перевіряє його."""
    number = int(input("Введіть додатне ціле число: "))
    return int(validate_positive_number(number))
