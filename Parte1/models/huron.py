

class Huron():

    def __init__(self,nombre, peso, edad, pais_origen, impuestos):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.pais_origen = pais_origen
        self.impuestos = impuestos

   
    def hacer_sonido(self):
        return "¡Eek Eek!"
    
    def calcular_flete(self):
        valor = self.impuestos * self.peso
        return valor


    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')

    @property
    def peso(self) -> int:
        """ Devuelve el valor del atributo privado 'peso' """
        return self.__peso
    
    @peso.setter
    def peso(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'peso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__peso = value
        else:
            raise ValueError('Expected int')
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self.__edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'edad'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__edad = value
        else:
            raise ValueError('Expected int')
    @property
    def pais_origen(self) -> str:
        """ Devuelve el valor del atributo privado 'pais_origen' """
        return self.__pais_origen
    
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'pais_origen'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__pais_origen = value
        else:
            raise ValueError('Expected str')
    @property
    def impuestos(self) -> int:
        """ Devuelve el valor del atributo privado 'impuestos' """
        return self.__impuestos
    
    @impuestos.setter
    def impuestos(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'impuestos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__impuestos = value
        else:
            raise ValueError('Expected int')
    @property
    def ratones_comido(self) -> int:
        return self.__ratones_comido
    @ratones_comido.setter
    def ratones_comido(self, value:int) -> None:
        if isinstance(value, int):
            self.__ratones_comido = value
        else:
            raise ValueError('Expected int')
