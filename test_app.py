import unittest
from app import sumar, multiplicar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
