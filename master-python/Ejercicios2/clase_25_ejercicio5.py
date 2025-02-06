'''Ejercicio 5.
Crea una lista con el contenido de esta tabla:
ACCION      AVENTURA     DEPORTES
GTA          ASSINS       FIFA 22
COD          CRASH        PRO 21
PUGB         POFP       MOTO GP 21

Mostrar esta informacion ordenada
'''

tabla = [
    {
        "categoria" : "ACCION",
        "juegos" : ["GTA","COD","PUGB"]
    },
    {
        "categoria" : "AVENTURA",
        "juegos" : ["ASSINS","CRASH","POFP"]
    },
    {
        "categoria" : "DEPORTES",
        "juegos" : ["FIFA 22","PRO 21","MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f'----------------{categoria['categoria']}----------------')
    for juego in categoria['juegos']:
        print(juego)