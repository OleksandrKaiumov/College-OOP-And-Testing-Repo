import pytest

from app import Figure


@pytest.fixture
def square():
    """Створює окремий квадрат з довжиною 10 для кожного тесту."""
    return Figure("квадрат", 10)


@pytest.fixture(scope="module")
def shared_rectangle():
    """Повертає один спільний прямокутник для тестів модуля."""
    return Figure("прямокутник", 10)
