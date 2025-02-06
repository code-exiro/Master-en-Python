'''Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje
segun el tipo de dato de cada variable. Usar funciones'''

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Numero"
    elif tipo == bool:
        result = "booleano"

    return result

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f'Este dato es del tipo {traducirTipo(tipo)}'
    else:
        result = None

    return result

mi_lista = ['hola gente', 2345]
titulo = 'Master en python'
numero = 1000
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo,str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero,bool))
