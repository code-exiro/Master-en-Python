'''Las funciones son bloques de código reutilizables diseñados para realizar una tarea específica. Las funciones pueden aceptar parámetros, devolver resultados y ayudar a estructurar el código de manera modular y clara'''

'''pass?
Estructurar funciones o clases vacías: Si estás definiendo una función, clase, o un bloque condicional, pero aún no quieres escribir el código completo, puedes usar pass como un marcador temporal. Esto evita errores de sintaxis porque Python no permite bloques vacíos.'''

'''DEFINICION DE UNA FUNCION

def nombre_funcion(parametros_opcionales):
    Cuerpo de la función
    pass  # Instrucción vacía''' 

    
#EJEMPLO

print('############# EJEMPLO 1 #############')

def saludar():
    print("Hola, mundo!")

saludar()  #llamar funcion

print('############# EJEMPLO 2 #############')

def muestraNombre():
    print("Victor")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")

muestraNombre() #Invocar funcion

print('############# EJEMPLO 3 #############')

nombre = 'Tyler'
edad = 17
nombreIngresado = input('ingresa tu nombre: ')
edadIngresada = int(input('Ingresa tu edad: '))

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print('Eres mayor de edad')
    else: 
        print("Eres menor de edad")

mostrarTuNombre(nombre, edad)
mostrarTuNombre('Kanye', 57)
mostrarTuNombre(nombreIngresado, edadIngresada)

print('############# EJEMPLO 4 #############')

def tablaFuncion(numero):
    print(f'Tabla de multiplificar del numero: {numero}\n')
    
    for tabla in range(11):
        print(f'{numero} X {tabla} = {numero * tabla}')

    print('\n')    

tablaFuncion(6)

print('############# EJEMPLO 4.1 #############')

for numeroTabla in range(1,11):
    tablaFuncion(numeroTabla)