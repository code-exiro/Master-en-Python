nombre = "Juan Perez"

#funciones generales
print(type(nombre)) #La funcion type se utiliza para obtener el tipo de dato o clase de un objeto
print('_____________________________________________')

#Detectar el tipado

'''La función isinstance() en Python se utiliza para comprobar si un objeto pertenece a un tipo o clase específica. Devuelve un valor booleano: True si el objeto pertenece al tipo o clase especificada, y False en caso contrario.'''

comprobar = isinstance(nombre, str)
if comprobar: #Si no se le pone nada es True, comprobar == True
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print('La variable no es un numero con decimales')
print('_____________________________________________')

#Limpiar espacios
frase = '       mi contenido          '
print(frase)
print(frase.strip()) #strip() es un metodo que elimina los espacio en blanco o caracteres especificos al inicio o al final de una cadena
print('_____________________________________________')

#Eliminar variables 
year = 2022
print(year)
del year
# print(year) ya fue eliminada entonces da error
print('_____________________________________________')

#Comprobar variable vacia
texto = '    ff    '

if len(texto) <= 0: #La funcion len() se utiliza para obtener la longitud de un objeto, 
    print("La variable esta vacia") #cadena de texto, lista, tupla, conjunto, diccionario, etc
else:
    print("La variable tiene contenido: ", len(texto)) #Devuelve un número entero que representa la cantidad de elementos en el objeto
print('_____________________________________________')

#Encontrar Posicion(indice) de una cadena 
frase = "La vida es bella, vida vieja" #Busca la posición(índice) de la primera aparición de una subcadena dentro de otra cadena
print(frase.find("vida")) #Si no se encuentra, devuelve -1
print('_____________________________________________')

#Reemplazar palabras en un String
nueva_frase = frase.replace("vida", "moto") #Se utiliza para reemplazar todas las ocurrencias de una subcadena
print(nueva_frase)
print('_____________________________________________')

#Mayusculas y minusculas
print(nombre) 
print(nombre.lower()) #Creo que es muy obvio 
print(nombre.upper())
print('_____________________________________________')
