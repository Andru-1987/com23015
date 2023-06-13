# Clase que no va a ser instanciada.
from oop_pack.Encapsulacion import Persona



'''
HERENCIA ABSTRACTA
'''
import abc
from abc import ABC

class PersonaAbstracta(ABC):

    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","unknown")
        self.email = kwargs.get("email","unknown")
        self.nacionalidad = kwargs.get("nacionalidad","unknown")
    
    @property
    def dni(self):
        pass

    @property
    def tramite(self):
        pass


# Es el heredado de una clase anterior
# class Jugador(Persona):  # cualquier clase
class Jugador(PersonaAbstracta):  # cualquier clase
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.club = kwargs.get("club","no creado")
        self.status = kwargs.get("status", True)

    def __str__(self):

        return f"""
        * CON ABSTRACCION muajajajaja

        Nombre:     {self.nombre}
        Email:      {self.email}
        Nac.:       {self.nacionalidad}
        dni :       {self.dni}
        tramite:    {self.tramite}
        ==========================

        Club:       {self.club}
        Status:     {self.status}
        """


    def get_status(self):
        return "SIGO JUGANDO" if self.status else "NO JUEGO MAS"

