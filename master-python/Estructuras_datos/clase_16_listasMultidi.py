'''Listas multidimensionales
listas multidimensionales en Python son listas que contienen otras listas como elementos'''

'''En una lista bidimensional, por ejemplo, cada lista anidada representa una fila, y los elementos dentro de esas listas representan las columnas'''

matriz = [
    [1, 2, 3],  # Fila 1
    [4, 5, 6],  # Fila 2
    [7, 8, 9]   # Fila 3
]
print(matriz[0]) # Salida: [1, 2, 3] (Primera fila)
print(matriz[1][0]) # Salida: 4 
print('_________________________________________')

#Iterar sobre listas multidimensionales
for fila in matriz:
    print(fila)
# Output:
# [1, 20, 3]
# [4, 5, 6]
# [7, 8, 9]
print('_________________________________________')

# Iterar por cada elemento
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
# Output: 1 20 3 4 5 6 7 8 9
print('\n_________________________________________\n')


print('######### Lista de contactos #########')
contactos = [
    [
        'Antonio',
        'antoniowawa@gmail.com'
    ],
    [
        'Luis',
        'luiswowo@gmail.com'
    ],
    [
        'Salvador',
        'salvadog@gmail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print('\n')

# print(contactos[2][1]) # Salida: salvadog@gmail.com