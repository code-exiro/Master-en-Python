'''---Ejercicio 8.
    -Cuanto es el X por ciento de X numero?
    -Ejemplo 20% de 2863'''

print("Cuanto es el X porcentaje de X numero?")

cantidad = int(input('Introduce la cantidad: '))
porcentaje = int(input(f'Que porcentaje quieres obtener de {cantidad}?: '))

operacion = (cantidad * porcentaje) / 100

print(f'El {porcentaje}% de {cantidad} es {operacion} lo que es igual a {cantidad - operacion}')