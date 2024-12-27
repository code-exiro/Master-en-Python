#Parametros opcionales 
print('\n############# EJEMPLO 5 #############')

def getEmpleado(nombre, dni = None):
    print('EMPLEADO')
    print(f'Nombre: {nombre}')

    if dni != None:
        print(f'DNI: {dni}')

getEmpleado('Tyler Robles Web, 256381')

print('\n############# EJEMPLO 6 #############') # return

def saludame(nombre):
    saludo = f'Hola, saludos {nombre}'

    return saludo

print(saludame('Kanye west'))

print('\n############# EJEMPLO 7 #############')

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += '\n'
        cadena += "Resta: " + str(resta)
        cadena += '\n'
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += '\n'
        cadena += "Division: " + str(division)
    else: 
        cadena += "Suma: " + str(suma)
        cadena += '\n'
        cadena += "Resta: " + str(resta)

    return cadena

print(calculadora(5, 5, True))

print('\n############# EJEMPLO 8 #############') #funciones dentro de otras

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + '\n' + getApellidos(apellidos)
    return texto

print(devuelveTodo('Tyler', 'The Creator'))

print('\n############# EJEMPLO 8 #############') 

'''funciones lambda
Son funciones anónimas que se definen en una sola línea y que no necesitan un nombre explícito (aunque puedes asignarlas a una variable si lo deseas).

lambda argumentos: expresión'''

#Ejemplo basico

suma = lambda a, b: a + b
print(suma(78,2))

print('\n############# EJEMPLO 9 #############') 

dime_el_año = lambda year: f"El año es {year}"
print(dime_el_año(2034))