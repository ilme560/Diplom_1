from data import BurgerData
class TestIngredient:

    def test_get_type_ingredients(self, ingredient):
        test_type = BurgerData.SAUCES_TYPE
        assert ingredient.get_type() == test_type

    def test_get_name_ingredients(self, ingredient):
        test_name = BurgerData.SAUCES_NAME
        assert ingredient.get_name() == test_name

    def test_get_price_ingredients(self, ingredient):
        test_price = BurgerData.SAUCES_PRICE
        assert ingredient.get_price() == test_price
