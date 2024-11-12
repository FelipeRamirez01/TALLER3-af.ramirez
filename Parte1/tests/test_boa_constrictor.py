import unittest
from models.boa_constrictor import Boa_Constrictor

class TestBoa(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Bella", 5, 10, "Colombia", 1500)  # nombre, edad, longitud

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 7500)  # Asumiendo que el flete es 5 * longitud

    def test_alimentar(self):
 
        self.boa.agregar_raton()
   
        try:
            self.boa.agregar_raton(5)
        except ValueError as e:
             print(e) 

        self.assertEqual(self.boa.ratones_comidos(), 6)
if __name__ == '__main__':
    unittest.main()