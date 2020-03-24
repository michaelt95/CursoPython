# Dado un diccionario, el cual almacena las calificaciones de un alumno,
# siendo las llaves los nombres de las materia y los valores las calificación,
# mostrar en pantalla el promedio del alumno.
# Ejemplo: calificaciones = {calculo:10, dibujo:5}

# calificaciones = {"calculo": 10, "dibujo": 5, "lengua": 7}

# notas = 0
#
# for asignaturas in calificaciones:
#     print(calificaciones[asignaturas])
#     notas += float(calificaciones[asignaturas])
# print("Promedio ",notas/3)

# A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.

# max_nota = max(list(calificaciones.values()))
# materia = " "
#
# for indice in calificaciones:
#     if calificaciones[indice] == max_nota:
#         materia = indice
#
# print("la materia", materia, "=", max_nota)

# Crear una lista la cual almacene 10 números positivos ingresados por el usuario,
# mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.

lista = []
contador = 0

while contador < 10:

    numero = float(input("dame 10 numeros positivos\n"))

    if numero >= 1:
        lista.append(numero)
        contador += 1
else:
    print("la Suma de los numeros:", sum(lista))
    print("El promedio:", sum(lista)/len(lista))
    print("El numero mayor:", max(lista))
    print("El numero menor:", min(lista))

#hacer luego los demas ejercicios