import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Oreo", 5, 10, "Colombia", 1500)  # nombre, edad, peso

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 7500)  # Asumiendo que el flete es 50 * peso

if __name__ == '__main__':
    unittest.main()