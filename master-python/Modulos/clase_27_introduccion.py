'''Un módulo es un archivo que contiene código (funciones, variables, clases, etc.) 
que puede ser reutilizado en otros programas. Los módulos permiten organizar el código en archivos más pequeños y mejorar su reutilización.

La carpeta __pycache__ en Python se genera automáticamente cuando ejecutas un script o importas un módulo.'''

# Importacion de modulo completo 
#import clase_26_primerModulo

#print(clase_26_primerModulo.holaMundo('Chamber'))
#print(clase_26_primerModulo.calculadora(35, 2, True))

# Importacion especifica
#from clase_26_primerModulo import holaMundo

#print(holaMundo("Victor Robles WEB"))

# Importacion global 
from clase_26_primerModulo import *

print(holaMundo('Chamber'))
print(calculadora(35, 2, True))
print('----------------------------')

# Modulo de fechas https://docs.python.org/es/3.13/library/datetime.html
import datetime
print("Modulo de fechas")

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())
print('----------------------------')

# Modulo matematicas
import math
print("Modulo matematicas")

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Numero pi: ", float(math.pi))

print("Redondear 6.63528 para arriba: ", math.ceil(6.63528))
print("Redondear 6.63528 para abajo: ", math.floor(6.63528))
print('----------------------------')

# Modulo random 
import random 
print("Modulo random")

print("Numero aleatorio entre 15 y 99: ", random.randint(15, 99))
print('----------------------------')
