import pytest
from data import BurgerData
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


@pytest.fixture(scope='function')
def bun():
    bun = Bun(name=BurgerData.BUNS_NAME, price=BurgerData.BUNS_PRICE)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(ingredient_type=BurgerData.SAUCES_TYPE, name=BurgerData.SAUCES_NAME, price=BurgerData.SAUCES_PRICE)
    return ingredient


@pytest.fixture(scope='function')
def mock():
    mock = Mock()
    return mock
