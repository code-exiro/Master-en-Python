'''Diccionarios
Un tipo de dato que almacena un conjunto de datos en formato clave > valor.
Esto significa que cada clave está asociada a un valor, y las claves deben ser únicas.

mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}'''

persona = {
    "nombre": "victor",
    "apellidos": "Robles",
    "web": "victorrobles.es"
}

print(persona) # Salida: {'nombre': 'victor', 'apellidos': 'Robles', 'web': 'victorrobles.es'}
print(persona["web"]) # Salida: victorrobles.es

#Usar get() para evitar errores si la clave no existe:
print(persona.get("ciudad"))  # Output: None
print('_________________________________________')

#Lista con diccionarios
contactos = [
    {
        'nombre': 'antonio',
        'email': 'antonioeloniio@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@gmail.com'    
    },
    {
        'nombre': 'salvadog',
        'email': 'salvadogdog@gmail.com'
    }
]

print(contactos) # Salida: [{'nombre': 'antonio', 'email': 'antonioeloniio@gmail.com'}, {'nombre': 'Luis', 'email': 'luis@gmail.com'}, {'nombre': 'salvadog', 'email': 'salvadogdog@gmail.com'}]

contactos[0]['nombre'] = 'Antona'
print(contactos[0]['nombre']) # Salida: Antona

print("\nListado de contactos: ")

for contacto in contactos:
    print(f'Nombre del contacto: {contacto['nombre']}')
    print(f'Email del contacto: {contacto['email']}')
    print('-------------------------------')