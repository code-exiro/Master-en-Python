# Bucles 

'''---for
for variable in secuencia:
    Código a ejecutar en cada iteración '''

frutas = ["manzana", "banana", "cereza"] #Secuencia iterable 
for fruta in frutas: #'fruta' es mi iteracion(cualquier otra puede ser mi iteracion como 'i')
    print(fruta)
print('-------------------------------------------------')

for i in range(5): #Función range() para generar un rango de números
    print(i)
print('-------------------------------------------------')

for i in range(1, 10, 2): #Se puede especificar un inicio, un final y un paso
    print(i)
print('-------------------------------------------------')

contador = 0 
resultado = 0 

for contador in range(0, 10):
    print(f"Voy por el {contador}")
    resultado += contador 

print(f"El resultado es: {resultado}")
print('-------------------------------------------------')

print("Tablas de multiplicar con for")
numero_usuario = int(input('De que numero quieres la tabla: '))

if numero_usuario < 1: 
    numero_usuario = 1 #Ajustando el numero en caso de que hayan puesto algo menor a 1

print(f'\n##### Tabla de multiplicar del {numero_usuario} #####')

for numero_tabla in range (1,11): #numero_tabla es mi iterable sobre range entonces sera todos en un rango del 1 al 10 

    if numero_usuario == 13: #Recordar que es un bucle en tonces dentro de este bucle podemos poner condicionales
        print("No se pueden mostrar numeros prohibidos")
        break

    print(f'{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}')
else:
    print('Tabla finalizada')

print('-------------------------------------------------')

'''---while
while condición:
    Código a ejecutar mientras la condición sea True
    
Si la condición nunca se vuelve False, el bucle será infinito '''

contador = 1

while contador <= 10:
    print(f'Estoy en el numero: {contador}')
    contador += 1

print('-------------------------------------------------')

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)
print('-------------------------------------------------')

print("Tablas de multiplicar con while")
numero_user = int(input('De que numero quieres la tabla: '))

if numero_user < 1:
    numero_user = 1

print(f'\n##### Tabla de multiplicar del {numero_user} #####')

contador = 1 
while contador <= 10:
    print(f'{numero_user} X {contador} = {numero_user*contador}')
    contador += 1
else: 
    print('Tabla finalizada')

print('-------------------------------------------------')

# Controlar bucles con break, continue 

# 'break' -> termina el bucle inmediatamente 

for i in range(10):
    if i == 5:
        break
    print (i)

# 'continue' -> salta a la siguiente iteración del bucle, ignorando el resto del código en esa iteración.

for i in range(5):
    if i == 2:
        continue
    print(i)
