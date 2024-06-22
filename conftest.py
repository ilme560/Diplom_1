import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


@pytest.fixture(scope='function')
def bun():
    bun = Bun(name='Флюоресцентная булка R2-D3', price=988)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(ingredient_type='Соусы', name='Соус традиционный галактический', price=15)
    return ingredient


@pytest.fixture(scope='function')
def mock():
    mock = Mock()
    return mock
