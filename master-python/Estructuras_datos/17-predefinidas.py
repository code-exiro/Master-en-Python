cantantes = ['2pac', 'Bad Bunny', 'Drake', 'Jose jose']
numeros = [1, 2, 5, 8, 3, 4]

#Ordenar
print(numeros)
numeros.sort()
print(numeros) # Salida: [1, 2, 3, 4, 5, 8]
print('____________________ 1 ____________________')

#Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1, 'David bisdal')
print(cantantes)
print('____________________ 2 ____________________')

#Eliminar elementos
cantantes.pop(1)
cantantes.remove('Bad Bunny')
print(cantantes)
print('____________________ 3 ____________________')

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)
print('____________________ 4 ____________________')

#Buscar dentro de una lista
print('Drake' in cantantes)
print('____________________ 5 ____________________')

#Contar elementos
print(cantantes)
print(len(cantantes))
print('____________________ 6 ____________________')

#Cuantas veces aparece un elemento 
numeros.append(8)
print(numeros.count(8))
print('____________________ 7 ____________________')

#Conseguir indice
print(cantantes.index("Drake"))
print('____________________ 8 ____________________')

#Unir listas
cantantes.extend(numeros)
print(cantantes)
print('____________________ 9 ____________________')




