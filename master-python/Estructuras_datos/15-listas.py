"""Listas(arrays)
Es una colección de elementos ordenados y mutables que se definen utilizando corchetes,
se divide en datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico.

mi_lista = [elemento1, elemento2, elemento3, ...]
"""

#Definir una lista
frutas = ["manzana", "banana", "cereza"]
cantantes = list(('bad','mamberroi','drake'))
years = list(range(10,30))
variada = ['victor', 122, 12.2, True, 'TEXTO']

print(frutas)  #Salida: ['manzana', 'banana', 'cereza']
print(cantantes)
print(years)
print(variada)
print('________________________1________________________')

#Acceso a elementos por índice
print(frutas[1]) #Salida: banana
print(frutas[-1]) #Salida: cereza (índice negativo accede desde el final)
print(frutas[1:3]) #Salida: ['banana', 'cereza']
print(frutas[0:]) #Salida: ['manzana', 'banana', 'cereza']
print(frutas[3:]) #Salida: []
print('________________________2________________________')

#Longitud de la lista
print(len(frutas))  #Salida: 3
print('________________________3________________________')

#Modificar elementos
frutas[1] = "mango"
print(frutas)  #Salida: ['manzana', 'mango', 'cereza']
print('________________________4________________________')

#Reemplazar elementos
frutas[0:2] = ["kiwi", "uva"]
print(frutas)  #Salida: ['kiwi', 'uva', 'cereza']
print('________________________5________________________')

#Agregar elementos
frutas.append("naranja") #append(): Agrega un elemento al final.
print(frutas)  #Salida: ['kiwi', 'uva', 'cereza', 'naranja']
print('________________________6________________________')

frutas.insert(1, "fresa") #insert(): Inserta un elemento en un índice específico.
print(frutas)  #Salida: ['kiwi', 'fresa', 'uva', 'cereza', 'naranja']
print('________________________7________________________')

#Eliminar elementos
frutas.remove("uva") #remove(): Elimina el primer elemento que coincida con el valor.
print(frutas)  #Salida: ['kiwi', 'fresa', 'cereza', 'naranja']
print('________________________8________________________')

fruta = frutas.pop(0) #pop(): Elimina y devuelve el elemento en un índice específico (por defecto el último).
print(fruta)  #Salida: kiwi
print('________________________9________________________')

frutas.clear() #clear(): Elimina todos los elementos de la lista.
print(frutas)  #Salida: []
print('________________________10________________________')
