'''---Ejercicio 1.
    -Crear variables una "pais" y otra "continente"
    -Mostrar su valor por pantalla (imprimir)
    -Poner un comentario diciendo el tipo de dato'''

pais = input('Escribe un pais: ')
continente = input('Escribe un continente: ')

print(type(pais))
print(type(continente))

print(f'El pais es: {pais} \nEl continente es: {continente}') #str, str
print('----------------------------------------------------')

'''---Ejercicio 2.
    -Escribir un script que nos muestre por pantalla todos los numeros pares del 1 al 120'''

for contador in range(1,121):
    if contador % 2 == 0:
        print(f'{contador} es par')
    #else:
    #    print(f'{contador} es impar')\

print('----------------------------------------------------')

'''---Ejercicio 3.
    -Escribir un programa que muestre los cuadrados 
    (un numero multiplicado por si mismo) de los primeros 60 
    numeros naturales. resolverlo con for y while'''

cuadrado = 1 

for contador in range(61):
    print(f"El cuadrado de: {contador} X {contador} = {contador * contador}")

while cuadrado <= 60:
    print(f'El cuadrado de: {cuadrado} X {cuadrado} es: {cuadrado * cuadrado}')
    cuadrado += 1