from io import open
import pathlib
import shutil
import os 

# Abrir archivo 
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "+a")
print(ruta)

# Escribir
archivo.write("********** Soy un texto introducido desde python **********\n")

# Cerrar archivo
archivo.close()

# Volver abrir archivo 
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")
print(ruta)

# Leer el contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer el contenido y guardar en lista 
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print("- " + frase.center(100))
#    if not frase.isnumeric():
#        print("- " + frase)
#    print("- " + frase.upper()) en mayusculas

'''# Copiar - import shutil
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

# Copiar a otra carpeta
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#ruta_alterna = "../Paquetes/fichero_copiado01.txt" # Primer forma
ruta_alterna = str(pathlib.Path().absolute()) + "/../Paquetes/fichero_copiado02.txt"

shutil.copyfile(ruta_original, ruta_alterna)

# Mover - lo comento porque que tal si me mueve algo por accidente 
ruta_original = str(pathlib.Path().absolute()) + "/../Paquetes/fichero_copiado01.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_de_PAQUETES.txt"

shutil.move(ruta_original, ruta_nueva)'''

# Eliminar archivos - import os
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)