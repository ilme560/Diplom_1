from praktikum.database import Database


class TestDataBase:
    def test_number_of_buns_in_database(self):
        test_database = Database()
        assert len(test_database.available_buns()) == 3

    def test_number_of_ingredients_in_database(self):
        test_database = Database()
        assert len(test_database.available_ingredients()) == 6