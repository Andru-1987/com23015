
from Jugador import Jugador
from Club import Club

river = Club(
    nombre_club     =   "river" ,
    division        =   "primera"
)

messi = Jugador(
    nombre  = "messi",
    edad    = 35,
    puesto  = "delantero",
    club    = "Rosario Central",
    activo  = False
)

riquelme = Jugador(
    nombre  = "riquelme",
    edad    = 33,
    puesto  = "delantero",
    club    = "boca jr" 
)

print(river.jugadores_fichados)

river.fichar_jugador(riquelme)
river.fichar_jugador(messi)
# print(river.jugadores_fichados)

river.mostrar_jugadores()

river.borrar_jugador("riquelme")
print("luego de borrar un jugador")
# print(river.jugadores_fichados)
river.mostrar_jugadores()

river.actualizar_status("messi")
river.mostrar_jugadores()

