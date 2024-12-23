'''---Ejercicio 10.
    -El programa tiene que pedir la nota de 15 alumnos
    y sacar por pantalla cuantos han aprobado y cuantos han suspendido'''

alumnos = 1 
aprobados = 0
reprobados = 0

print('######### CALIFICACIONES #########')

while alumnos <= 5:
    calificacion = int(input(f'Alumno {alumnos} ingresa tu calificacion: '))

    if calificacion >= 6 and calificacion <= 10:
        print(f'{calificacion} es una calificacion aprobatoria ')
        alumnos += 1
        aprobados += 1
    elif calificacion > 10:
        print(f'{calificacion} es una calificacion invalida')
    else:
        print(f'{calificacion} tas reprobado')
        alumnos += 1
        reprobados += 1

print(f'hay {aprobados} alumnos aprobados y {reprobados} alumnos reprobados')
    