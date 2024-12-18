'''---Ejercicio 9.
    -Hacer un programa que pida numeros al usuario
    infinitamente hasta que introdusca el 111'''

print('######## Adivina la clave de 3 dígitos ########')

numero = 0

while True:
    numero = int(input('Digita un número: '))

    if numero == 111:
        print(f'Clave correcta {numero} ✔️')
        break
    else:
        print('Clave incorrecta ❌. Intenta nuevamente.')


