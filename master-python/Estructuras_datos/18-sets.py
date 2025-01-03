'''Sets
Son una estructura de datos que representa una colección no ordenada, mutable y que no permite elementos duplicados.

Estructura basica
Se define un set utilizando llaves { } o el constructor set().

mi_set = {elemento1, elemento2, elemento3, ...}
'''

mi_set = {4, 5, 2 ,1}
print(mi_set)  # Salida: {1, 2, 3, 4}

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")

print(type(personas)) # <class 'set'>
print(personas) # {'Manolo', 'Victor', 'Paco'}

