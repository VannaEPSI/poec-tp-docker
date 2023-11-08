#Tester les fonctions

import unittest
from calc import apply_percent

class TestCalcMethods(unittest.TestCase):

    def test_nominal_case(self):
        print('Début du test nominal')
        new_price = apply_percent(100, 20)
        self.assertEqual(new_price, 120)
        print('Fin du test')

    def test_virgule_case(self):
        print('Début du test virgule')
        new_price = apply_percent(55.25, 5.5)
        self.assertEqual(new_price, 58.28874999999999)
        print('Fin du test')

    def test_price_nulle_case(self):
        print('Début du test price 0')
        new_price = apply_percent(0, 10)
        self.assertEqual(new_price, 0)
        print('Fin du test')

    def test_price_negative_case(self):
        print('Début du test prix négatif')
        new_price = apply_percent(-10.99, 10)
        self.assertEqual(new_price, 'Price ($-10.99) is negative')
        print('Fin du test')

    def test_wrong_value_case(self):
        print('Début du test wrong value')
        new_price = apply_percent('abc', 10)
        self.assertEqual(new_price, 'Price (abc) is not a number')
        print('Fin du test')

    def test_percent_negative_case(self):
        print('Début du test pourcentage négatif')
        new_price = apply_percent(10, -10)
        self.assertEqual(new_price, 'Percent (-10) is negative')
        print('Fin du test')

    def test_percent_over_100_case(self):
        print('Début du test pourcentage supérieur')
        new_price = apply_percent(100, 110)
        self.assertEqual(new_price, 'Percent (110) is superior to 100%')
        print('Fin du test')


if __name__ == '__main__':
    unittest.main()