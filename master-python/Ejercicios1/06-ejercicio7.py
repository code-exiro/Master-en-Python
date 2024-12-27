'''---Ejercicio 7.
    -Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario'''

numero1 = int(input('Introduce el primer numero: '))
numero2 = int(input('Introduce el segundo numero: '))

if numero1 < numero2:

    for contador in range(numero1, numero2 + 1):

        if contador % 2 == 0:
            print(f'{contador} Par')
        else:
            print(f'{contador} No par')

else:
    print('El primer número debe ser menor que el segundo.')




