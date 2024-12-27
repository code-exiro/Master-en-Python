#Parametros opcionales 

def getEmpleado(nombre, dni = None):
    print('EMPLEADO')
    print(f'Nombre: {nombre}')

    if dni != None:
        print(f'DNI: {dni}')

getEmpleado('tyler', 27252)