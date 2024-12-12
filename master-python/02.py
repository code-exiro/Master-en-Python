# Condicionales

'''---if else
if condición:
    Código que se ejecuta si la condición es verdadera
else:
    Código si la condición es falsa'''

print('################ EJEMPLO 1 ################')
color = input("Adivina cual es mi color favorito: ")

if color == 'rojo':
    print('Correcto')
    print('El color es rojo')
else:
    print('Color incorrecto')
print('-----------------------------------------------------')

print('################ EJEMPLO 2 ################')
edad = int(input('Que edad tienes?: '))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
print('-----------------------------------------------------')

'''---elif
if condición1:
    Código si la condición1 es verdadera
elif condición2:
    Código si la condición2 es verdadera
else:
    Código si ninguna condición es verdadera'''

print('################ EJEMPLO 3 ################')
edad = int(input('Que edad tienes?: '))

if edad < 18:
    print("Eres menor de edad.")
elif edad < 60:
    print("Eres un adulto.")
else:
    print("Eres una persona mayor.")

print('################ EJEMPLO 4 ################')
dia = int(input('Escoje un numero del 1 al 7: '))

if dia == 1:
    print('Lunes')
elif dia  == 2:
    print('Martes')
elif dia == 3:
    print('Miercoles')
elif dia == 4:
    print('Jueves')
elif dia == 5:
    print('Viernes')
elif dia == 6:
    print('Sabado')
else:
    print('Domingo')
print('-----------------------------------------------------')

# ifs anidados

print('################ EJEMPLO 5 ################')
edad = int(input("Que edad tienes: "))
nombre = input("Cual es tu nombre: ")
continente = input("En que continente habitas: ")
ciudad = input("En que ciudad estas: ")
mayoria_de_edad = 18

if edad >= 18: # Entre mas if se cumplan mas condiciones se van a imprimir 
    print(f'eres mayor de edad {nombre}')
    if continente == 'america':
        print(f'Eres de america {nombre}')
        if ciudad != 'mexico':
            print(f'Eres de alguna parte de america')
        else:
            print(f'Eres Mexicano {nombre}')
    else:
        print(f'No eres de america')
else:
    print(f'eres menor de edad {nombre}')
print('-----------------------------------------------------')

# ejemplos de un if con un operadores logicos

print('################ EJEMPLO 6 ################')
edad_minima = 18
edad_maxima = 70
edad_oficial = int(input('Tienes edad para trabajar? Introduce tu edad '))

if edad_oficial >= 18 and edad_oficial <= 70:
    print("Estas en edad de trabajar")
else:
    print("Aun estas verde")
print('-----------------------------------------------------')

print('################ EJEMPLO 6 ################')
pais = "Rusia"

if pais == "Mexico" or pais == "Argentina" or pais == "Colombia":
    print(f'{pais} es un pais de habla hispana')
else: 
    print(f'{pais} no es un pais de habla hispana')   
print('-----------------------------------------------------')

