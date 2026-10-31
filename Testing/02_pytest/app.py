from math import isfinite


class Figure:
    """Геометрична фігура з додатною скінченною довжиною сторони."""

    FIGURES = ("квадрат", "прямокутник", "трикутник")
    ANGLES = {
        "квадрат": 4,
        "прямокутник": 4,
        "трикутник": 3,
    }

    def __init__(self, figure_type: str, length: int | float) -> None:
        assert isinstance(length, (int, float)) and not isinstance(length, bool), (
            "Довжина має бути числом!"
        )
        assert not isinstance(length, float) or isfinite(length), (
            "Довжина має бути скінченним числом!"
        )
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
        return self.ANGLES[self.type]
