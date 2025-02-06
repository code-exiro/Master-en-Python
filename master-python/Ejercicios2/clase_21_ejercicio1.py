'''Ejercicio 1. 
Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
    -Recorrer la lista y mostrarla 
    -Hacer una funcion que recorra listas de numeros y devuelva un string
    -Ordenarla y mostrarla
    -Mostrar su longitud
    -Buscar algun elemento (que el usuario pida por teclado)'''

lista = []

def recorrer_lista(lista):
    resultado = ""
    for i in range(len(lista)):
        resultado += f'Elemento {i+1}: {lista[i]}, '
    return resultado.strip(', ')

def buscar_elemento(lista):
    elemento_buscado = int(input("¿Qué número deseas buscar en la lista? "))
    if elemento_buscado in lista:
        posicion = lista.index(elemento_buscado) + 1
        return f"El número {elemento_buscado} está en la posición {posicion}."
    else:
        return f"El número {elemento_buscado} no está en la lista."

# Llenar la lista con 8 números
for numeros in range(8):
    numeroExtra = int(input('Ingresa un número entero: '))
    lista.append(numeroExtra)

# Mostrar los números ingresados
print('\nTus Números son:')
for i in range(len(lista)):
    print(f'Número {i+1}: {lista[i]}')

# Ordenar y mostrar la lista
print('\nLos números ordenados quedan así:')
lista.sort()
print(lista)

# Mostrar la cantidad de números
print(f'Son un total de {len(lista)} números.')

# Mostrar los números de la lista como string
print('\nLista recorrida funcion:')
print(recorrer_lista(lista))

# Buscar un número en la lista
print('\nResultado de la búsqueda:')
print(buscar_elemento(lista))

'''Que aprendi de este ejercicio?

Me di cuenta de que necesito mejorar mi capacidad para analizar y discernir los problemas que se me presentan. Durante esta tarea, me compliqué demasiado pensando en lo que me pedían, cómo me lo pedían y en cuál sería la mejor manera de implementarlo.

Creo que pude haber abordado la solución de una manera más eficiente. Por ejemplo, si hubiera comentado el código desde el principio, habría tenido más claridad sobre lo que hacía cada parte del programa, lo que también me habría facilitado hacer ajustes y correcciones.

A pesar de haber terminado, el resultado final no me deja satisfecho. Siento que podría haber tomado un enfoque diferente. Es importante organizar mis ideas antes de comenzar a desarrollar, priorizar la claridad y documentar mi trabajo desde el inicio.'''