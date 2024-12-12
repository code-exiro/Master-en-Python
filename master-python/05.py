'''---Ejercicio 4.
    -Pedir dos numeros al usuario y hacer todas las operaciones 
    basicas de una calculadora y mostrarlo por pantalla '''

numero1 = int(input('Ingresa un numero: '))
numero2 = int(input('Ingresa un numero: '))

def Operaciones(numero1, numero2):
    print(f"Suma: {numero1} + {numero2} = {numero1 + numero2}")
    print(f"Resta: {numero1} - {numero2} = {numero1 - numero2}")
    print(f"Multiplicacion: {numero1} * {numero2} = {numero1 * numero2}")
    print(f"Division: {numero1} / {numero2} = {numero1 / numero2}")

Operaciones(numero1, numero2)
print('-----------------------------------------------------')

'''---Ejercicio 5.
    -Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario '''

numero1 = int(input('Ingresa un numero: '))
numero2 = int(input('Ingresa un numero: '))

if numero1 < numero2:
    for contador in range(numero1, numero2 + 1):
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")

print('-----------------------------------------------------')