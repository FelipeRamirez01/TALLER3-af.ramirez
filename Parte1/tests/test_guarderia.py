import unittest
from models.guarderia import Guarderia

class TestGuarderia(unittest.TestCase):

    def setUp(self):
        self.guarderia = Guarderia()
   
    def test_alimentar_guarderia(self):
        
        self.assertEqual(self.guarderia.alimentar_boa(self.guarderia.boa1, 8), "Éxito")
        self.assertEqual(self.guarderia.alimentar_boa(self.guarderia.boa1, 3), "La boa está llena")
        self.assertEqual(self.guarderia.alimentar_boa(None, 11), "Esta Boa no existe!")


if __name__ == '__main__':
    unittest.main()