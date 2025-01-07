'''Ejercicio 2.
Escribir un programa que añada valores a una lista mientras que 
su longitud sea menor a 120 y luego mostrar la lista'''

import random

lista = []

print('#### Menos de 120 ####')
longitud = int(input("De cuantos numeros quieres la lista?: "))

eleccion = (input("Como te gustaria resolver el ejercicio 'for' o 'while': "))
contador = 1

if longitud <= 120:
    if eleccion == 'for':
        for anadir in range(longitud):
            añadirNumero = random.randint(1,999)
            lista.append(añadirNumero)
        print(f'Son un Total de {len(lista)} elementos con for: ')
        print(lista)
    elif eleccion == 'while':
        while contador <= longitud:
            añadirNumero = random.randint(1,999)
            lista.append(añadirNumero)
            contador += 1
        print(f'Son un Total de {len(lista)} elementos con while: ')
        print(lista)
    else:
        print(f'Eleccion "{eleccion}" no valida')
else:
    print(f'Rango no disponible {longitud}')

'''Que aprendi en este ejercicio?
Me gusto mucho mas como resolvi este que el anterior primero hice lo que me pidieron y 
despues fui agregando cosas que crei que quedarian bien, igual y se me paso documentar el codigo,
pero me dejo mucho mejor sensacion este ejercicio'''