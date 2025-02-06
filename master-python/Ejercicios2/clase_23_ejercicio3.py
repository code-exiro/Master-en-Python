'''Ejercicio 3.
Programa que compruebe si una variable esta vacia y si esta vacia, 
rellenarla con texto en minusculas y mostrarlo en mayusculas'''

import time

def revision_texto():
    while True:
        texto = input('Ingresa un texto en minúsculas: ').strip()
        
        print('Revisando el texto...')
        time.sleep(2)

        if len(texto) == 0:
            print('El texto está vacío. Inténtalo de nuevo.')
            continue

        if texto != texto.lower():
            print(f'Error: Ingresa "{texto}" en minúsculas.')
        else:
            print(f'El texto "{texto}" está en minúsculas ✅')
            return texto.upper()

# Llamada a la función
resultado = revision_texto()
print(f'Texto convertido a MAYÚSCULAS: {resultado}')













'''
def revision_texto(texto):

    if len(texto) == 0:
        print('El texto esta vacio rellenalo con minusculas: ')
        texto = input('Ingresa el texto: ')

        if texto == texto.lower():
            print('El texto esta en minusculas es correcto')
            print(texto.upper())
        else:
            print('todo mal')

    else:
        print('El texto no esta vacio')
'''
