'''Variables locales: Se definen dentro de la funcion y no se puede usar fuera de ella, 
solo estan disponibles dentro a no ser que hagamos un return

Variables globales: Son las que se declaran fuera de una funcion y estan disponibles dentro y fuera de ellas'''

#Variable global 
frase = "Ni los genios son tan genios ni los mediocres tan mediocres"

print(frase)
print('________________________________________________________')

def holaMundo():
    frase = "Hola mundo"
    print('Dentro de la funcion')
    print(frase)

    year = 2021
    print(year)

    global website
    website = "nandezweb.es.com"
    print("Dentro: ", website)

    return "Dato retornado " + str(year) 
'''El return representa el "valor" de la función, antes de usar return, la función ejecuta todos los print,
ahora si yo la pongo dentro de un print me mostrara lo que vale la funcion en si misma '''

print(holaMundo())
print("Fuera: ", website)
print('________________________________________________________')
holaMundo()
