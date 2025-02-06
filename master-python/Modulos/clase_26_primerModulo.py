def holaMundo(nombre):
    return f"Hola como estas {nombre}"

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += '\n'
        cadena += "Resta: " + str(resta)
        cadena += '\n'
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += '\n'
        cadena += "Division: " + str(division)
    else: 
        cadena += "Suma: " + str(suma)
        cadena += '\n'
        cadena += "Resta: " + str(resta)

    return cadena
