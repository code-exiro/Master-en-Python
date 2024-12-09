# Esto es un comentario, el cual no se mostrara en la ejecucion

print("Aca hay un comentario")
print('Aca hay un comentario ')

'''
Puedes hacer 
comentarios de varias 
lineas con 3 comillas
'''

"""
ya sean simples o dobles 
como en este caso 
"""

print('Adios')
print('---------------------------------------------------------------')


'''
---Variables 
En Python, no es necesario declarar explícitamente el tipo de una variable.
Estas son contenedoras de informacion.
'''

texto = "Master en python"
texto2 = "Con Emir"
numero = 56
decimal = 4.3

print(texto)
print(texto2)
print(numero)
print(decimal)
print('---------------------------------------------------------------')

numero = 77  # Se sustiyo el contenido de las variables anterioremente declaradas.
decimal = 8.9  # Reasignacion de valores.

print(numero)  
print(decimal)
print('---------------------------------------------------------------')

# Concatenacion

nombre = "Emir"
apellido = "Erizo"
web = "Emirizoweb.com"

print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))
print('---------------------------------------------------------------')

# Tipos de datos

nada = None
cadena = "Hola mi gente"
entero = 99
flotante = 5.3
booleano = False
lista = [10, 12, 23, 34, 56]
listaString = [34, "treinta", 34, "horale"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre" : "Emir",
    "apellido" : "Erizo",
    "curso" : "Master en python"
}
rango =  range(7)
dato_byte = b"aprobado"

print(dato_byte)
print(type(dato_byte))
print('---------------------------------------------------------------')

''' Casting 
El proceso de convertir un dato de un tipo a otro, 
arriba vimos los tipos de datos
'''

texto3 = 'aca tenemos un texto'
numerito = str(777) 

print(type(numerito))
print(texto3 + " " + numerito)

numerito = int(777)
print(type(numerito))

numerito = float(777)
print(type(numerito))
print('---------------------------------------------------------------')

# Detalles

mi_texto = '"Master"'
mi_texto2 = "en \"Python\" " # para imprimir las comillas 

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

texto_unido = mi_texto + " \n " + mi_texto2 # salto de linea
print(texto_unido)

texto_unido = mi_texto + " \t " + mi_texto2 # tabulacion 
print(texto_unido)

texto_unido = mi_texto + " \r " + mi_texto2 # borra lo que hay detras
print(texto_unido)
print('---------------------------------------------------------------')


#---Operadores en python

# Operadores aritmeticos
suma = 5 + 3  # 8
resta = 5 - 3  # 2
multiplicacion = 5 * 3  # 15
division = 5 / 2  # 2.5
division_entera = 5 // 2  # 2
modulo = 5 % 2  # 1
exponente = 2 ** 3  # 8

# Operadores de comparacion(relacionales)
5 == 5  # True
5 != 3  # True
5 > 3  # True
5 < 3  # False
5 >= 5  # True
5 <= 3  # False

# Operadores logicos
True and False  # False
True or False  # True
not True  # False

# Operadores de asignacion
x = 5 # Asignación básica
x += 3 # Suma y asigna
x -= 3 # Resta y asigna
x *= 3 # Multiplica y asigna
x /= 3 # Divide y asigna
x //= 3 # División entera y asigna
x %= 3 # Módulo y asigna
x **= 3 # Exponente y asigna

# Operadores de pertencia
'a' in 'hola'  # True
'z' not in 'hola'  # True

# Operadores de identidad
x = [1, 2] # is : Devuelve True si los objetos son el mismo.
y = x
x is y  # True

x = [1, 2] # is not : Devuelve True si los objetos no son el mismo.
y = [1, 2]
x is not y  # True
print('---------------------------------------------------------------')

