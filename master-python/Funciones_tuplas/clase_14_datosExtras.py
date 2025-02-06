# Lo recomendable y para tenerlo en cuenta es que es muy importante que las funciones retornen algo (return)

def mi_funcion(nombre):
    return "Hola que tal" + nombre

def mi_segunda_funcion(apellidos):
    return "Hola que tal 2" + apellidos

nombre = "Victor"
apellidos = "Robles"

print(mi_funcion())
print(mi_segunda_funcion())