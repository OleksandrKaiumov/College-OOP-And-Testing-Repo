import pytest

from app import Figure


@pytest.mark.unit
def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.unit
def test_square_properties(square):
    assert square.type == "квадрат"
    assert square.get_figure_type == "квадрат"
    assert square.get_figure_length == 10
    assert square.get_angles == 4


@pytest.mark.parametrize(
    "figure_type", Figure.FIGURES, ids=["square", "rectangle", "triangle"]
)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type


@pytest.mark.parametrize("length", [1, 10, 2.5, 0.1])
def test_valid_length(length):
    assert Figure("квадрат", length).get_figure_length == length


@pytest.mark.parametrize(
    "figure_type",
    [
        pytest.param("коло", id="circle"),
        pytest.param("шестикутник", id="hexagon"),
        pytest.param("", id="empty"),
        pytest.param("КВАДРАТ", id="uppercase"),
        pytest.param(" квадрат ", id="spaces"),
        pytest.param(None, id="none"),
        pytest.param(123, id="integer"),
        pytest.param(True, id="boolean"),
        pytest.param(["квадрат"], id="list"),
        pytest.param({"type": "квадрат"}, id="dictionary"),
    ],
)
def test_invalid_figure(figure_type):
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 1)


@pytest.mark.parametrize(
    "length, message",
    [
        pytest.param(0, "більшою за 0", id="zero"),
        pytest.param(-1, "більшою за 0", id="negative-integer"),
        pytest.param(-2.5, "більшою за 0", id="negative-float"),
        pytest.param("10", "має бути числом", id="string"),
        pytest.param("", "має бути числом", id="empty-string"),
        pytest.param(None, "має бути числом", id="none"),
        pytest.param(True, "має бути числом", id="true"),
        pytest.param(False, "має бути числом", id="false"),
        pytest.param([10], "має бути числом", id="list"),
        pytest.param({"length": 10}, "має бути числом", id="dictionary"),
        pytest.param(1 + 2j, "має бути числом", id="complex"),
        pytest.param(float("nan"), "скінченним числом", id="nan"),
        pytest.param(float("inf"), "скінченним числом", id="positive-infinity"),
        pytest.param(float("-inf"), "скінченним числом", id="negative-infinity"),
    ],
)
def test_invalid_length(length, message):
    with pytest.raises(AssertionError, match=message):
        Figure("квадрат", length)


def test_module_fixture_type(shared_rectangle):
    assert shared_rectangle.get_figure_type == "прямокутник"


def test_module_fixture_length(shared_rectangle):
    assert shared_rectangle.get_figure_length == 10
