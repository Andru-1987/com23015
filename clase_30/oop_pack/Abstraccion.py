# Clase que no va a ser instanciada.
from oop_pack.Encapsulacion import Persona



'''
HERENCIA ABSTRACTA
'''
import abc
from abc import ABC

class PersonaAbstracta(ABC):

    __dni = None
    __tramite = None

    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","unknown")
        self.email = kwargs.get("email","unknown")
        self.nacionalidad = kwargs.get("nacionalidad","unknown")

    
    @abc.abstractmethod
    def set_dni(self,dni):
        ...
    @abc.abstractmethod
    def get_dni(self):
        ...
    @abc.abstractmethod
    def set_tramite(self,tramite):
        ...
    @abc.abstractmethod
    def get_tramite(self):
        ...



# Es el heredado de una clase anterior
# class Jugador(Persona):  # cualquier clase
class Jugador(PersonaAbstracta):  # cualquier clase
    def __init__(self,**kwargs):
        self.club = kwargs.get("club","no creado")
        self.status = kwargs.get("status", True)
        super().__init__(**kwargs)

    def __str__(self):

        return f"""
        * CON ABSTRACCION muajajajaja

        Nombre:     {self.nombre}
        Email:      {self.email}
        Nac.:       {self.nacionalidad}
        dni :       {self.get_dni()}
        tramite:    {self.get_tramite()}
        ==========================

        Club:       {self.club}
        Status:     {self.status}
        """


    def get_status(self):
        return "SIGO JUGANDO" if self.status else "NO JUEGO MAS"

      
    def set_dni(self,dni):
        self.__dni = dni
    
    def get_dni(self):
        return self.__dni
    
    def set_tramite(self,tramite):
        self.__tramite = tramite
    
    def get_tramite(self):
        return self.__tramite