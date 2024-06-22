
class TestIngredient:

    def test_get_type_ingredients(self, ingredient):
        test_type = "Соусы"
        assert ingredient.get_type() == test_type

    def test_get_name_ingredients(self, ingredient):
        test_name = 'Соус традиционный галактический'
        assert ingredient.get_name() == test_name

    def test_get_price_ingredients(self, ingredient):
        test_price = 15
        assert ingredient.get_price() == test_price
