from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron


class Guarderia:
    def __init__(self):
        # Crear dos boas y dos hurones
        self.boa1 = Boa_Constrictor("Bella", 5, 10, "Colombia", 1500)
        self.boa2 = Boa_Constrictor("Linda", 5, 10, "Colombia", 1500)
        self.huron1 = Huron("Oreo", 5, 10, "Colombia", 1500)
        self.huron2 = Huron("Galleta", 5, 10, "Colombia", 1500)
    
    def alimentar_boa(self, boa, ratones):
        # Verificar si la boa es None
        if boa is None:
            return "Esta Boa no existe!"
        
        # Intentar alimentar a la boa
        try:
            boa.agregar_raton(ratones)  # Llamar al método para agregar un ratón
            return "Éxito"
        except ValueError as e:
            return "La boa está llena"
