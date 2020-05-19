import unittest
from city_function import cities_in_countries


class CityTestCase(unittest.TestCase):
    """测试cities_in_countries"""

    def test_city_country(self):
        city_in_country = cities_in_countries('santiago', 'chile')
        self.assertEqual('Santiago, Chile', city_in_country)

    def test_city_country_population(self):
        city_country_population = cities_in_countries('santiago', 'chile', 456456456)
        self.assertEqual('Santiago, Chile - Population 456456456', city_country_population)


unittest.main()
