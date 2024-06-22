
class TestBun:

    def test_get_name_buns(self, bun):
        test_name = 'Флюоресцентная булка R2-D3'
        assert bun.get_name() == test_name

    def test_get_price_buns(self, bun):
        test_price = 988
        assert bun.get_price() == test_price
