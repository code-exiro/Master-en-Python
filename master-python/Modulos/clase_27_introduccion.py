'''Un módulo es un archivo que contiene código (funciones, variables, clases, etc.) 
que puede ser reutilizado en otros programas. Los módulos permiten organizar el código en archivos más pequeños y mejorar su reutilización.'''

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

# Modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now