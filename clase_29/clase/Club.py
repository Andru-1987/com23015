from Jugador import Jugador

class Club:

    jugadores_fichados = []

    def __init__(self,**kwargs):
        self.nombre_club = kwargs['nombre_club']
        self.division = kwargs['division']
    
    def __str__(self):
        return f"""
            nombre del club : {self.nombre_club}
            division        : {self.division}
        """

    def mostrar_jugadores(self):
        for jugador in self.jugadores_fichados:
            print(jugador.presentar())

    def fichar_jugador(self, jugador:Jugador):
        self.jugadores_fichados.append(jugador)
        print(f"Se ha agregado:\n{jugador.nombre}")

    def borrar_jugador(self, nombre:str):
        # for index,jugador in enumerate(self.jugadores_fichados):
        #     if jugador.nombre == nombre:
        #         self.jugadores_fichados.pop(index)

        self.jugadores_fichados = [
            jugador for jugador in self.jugadores_fichados if jugador.nombre != nombre 
        ]
    def actualizar_status(self, nombre:str):

        for jugador in self.jugadores_fichados:
            if jugador.nombre == nombre:
                jugador.activo = not jugador.activo
