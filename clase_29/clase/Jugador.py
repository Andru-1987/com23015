

class Jugador:
    # def __init__(self, nombre, edad, puesto,club, activo=True):
        # self.nombre:str = nombre
        # self.edad:int = edad
        # self.puesto:str = puesto
        # self.club:str = club
        # self.activo:bool = activo
    
    def __init__(self,**kwargs):
        self.nombre:str = kwargs["nombre"]
        self.edad:int = kwargs["edad"]
        self.puesto:str = kwargs["puesto"]
        self.club:str = kwargs["club"]
        self.activo:bool = kwargs.get("activo" , True)


    def presentar(self):
        return f"Hola! Soy {self.nombre}, tengo {self.edad} años y estoy en club {self.club}\n {self.mostrar_activo()}"

    def mostrar_activo(self):
        if self.activo:
            return "Estoy trabajando activamente"
        else:
            return "Ya me jubile"