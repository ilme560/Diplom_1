from data import BurgerData
class TestBun:

    def test_get_name_buns(self, bun):
        test_name = BurgerData.BUNS_NAME
        assert bun.get_name() == test_name

    def test_get_price_buns(self, bun):
        test_price = BurgerData.BUNS_PRICE
        assert bun.get_price() == test_price
