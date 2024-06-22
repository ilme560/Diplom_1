from data import BurgerData
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self, mock, burger):
        mock.get_name.return_value = BurgerData.BUNS_NAME
        mock.get_price.return_value = BurgerData.BUNS_PRICE
        burger.set_buns(mock)
        assert burger.bun.get_name() == BurgerData.BUNS_NAME and burger.bun.get_price() == BurgerData.BUNS_PRICE

    def test_add_ingredient(self, burger, mock):
        mock.get_type.return_value = BurgerData.FILLINGS_TYPE
        mock.get_name.return_value = BurgerData.FILLINGS_NAME
        mock.get_price.return_value = BurgerData.FILLINGS_PRICE
        burger.add_ingredient(mock)
        assert burger.ingredients == [mock]

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        ingredient_0 = Ingredient(BurgerData.FILLINGS_TYPE, BurgerData.FILLINGS_NAME, BurgerData.FILLINGS_PRICE)
        ingredient_1 = Ingredient(BurgerData.SAUCES_TYPE, BurgerData.SAUCES_NAME, BurgerData.SAUCES_PRICE)
        burger.add_ingredient(ingredient_0)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1].name == BurgerData.FILLINGS_NAME

    def test_get_price(self, bun, burger):
        burger.set_buns(bun)
        burger.add_ingredient(Ingredient(BurgerData.FILLINGS_TYPE, BurgerData.FILLINGS_NAME, BurgerData.FILLINGS_PRICE))
        burger.add_ingredient(Ingredient(BurgerData.SAUCES_TYPE, BurgerData.SAUCES_NAME, BurgerData.SAUCES_PRICE))
        assert burger.get_price() == BurgerData.BURGER_PRICE

    def test_get_receipt(self, mock, burger):
        mock.get_name.return_value = BurgerData.BUNS_NAME
        mock.get_price.return_value = BurgerData.BUNS_PRICE
        burger.set_buns(mock)
        burger.add_ingredient(Ingredient(BurgerData.FILLINGS_TYPE, BurgerData.FILLINGS_NAME, BurgerData.FILLINGS_PRICE))
        burger.add_ingredient(Ingredient(BurgerData.SAUCES_TYPE, BurgerData.SAUCES_NAME, BurgerData.SAUCES_PRICE))
        assert burger.get_receipt() == BurgerData.BURGER_RECIPE
