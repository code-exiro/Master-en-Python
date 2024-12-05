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

#---Operadores en python

# Operadores aritmeticos

suma = 2 + 4
resta = 2 - 3

