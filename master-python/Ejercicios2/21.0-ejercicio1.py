"""lista = [1,3,5,7,8,9,3,5]

print(len(lista))
print(lista)

if len(lista) == 8:
    print("La lista tiene 8 caracteres")
else:
    print("algo estamos haciendo mal")

numeroExtra = int(input('Ingresa un numero mas a la lista: '))
lista.append(numeroExtra)

print(len(lista))
print(lista)

if len(lista) == 8:
    print("La lista tiene 8 caracteres")
else:
    print("igual y no estamos tan mal")
"""
numeros = [13, 45, 34, 34, 34, 23, 92, 67]

def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"

print(' ###########  ')