from oop_pack.Encapsulacion import Persona
from oop_pack.Abstraccion import PersonaAbstracta
from oop_pack.Abstraccion import Jugador

print("PRIMER PASO DE ENCAPSULACION")



mateo = Persona(
    nombre  =   "mateo",
    email   =   "mateo@mail.com",
    nacionalidad    =   "mexico"
)


print(mateo)
mateo.set_dni(19998822)
mateo.set_tramite("gt-123-ade")
print(mateo)

# print("Te permite mostrarlo aunque no es lo más hermoso =>\t",mateo._Persona__dni)
# print(mateo.__dni)


print("HERENCIA--> CASI CASI ABSTRACCION")

mateo_jugador = Jugador(
    nombre  =   "mateo",
    email   =   "mateo@mail.com",
    nacionalidad    =   "mexico",
    status          = True ,
    club    =   "Sacachispas"
)

print(mateo_jugador)

"""
ABSTRACCION NO ME PERMITE CREAR 

l_gante = PersonaAbstracta(
    nombre  =   "l-gante",
    email   =   "l.gante@mail.com",
    nacionalidad    =   "argentina"
)


print(l_gante)
"""