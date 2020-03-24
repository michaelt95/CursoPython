# Dado de los valores ingresados por el usuario (base, altura)
# calcular y mostrar en pantalla el área de un triángulo.

# base = float(input("Dame la base\n"))
# altura = float(input("dame la altura\n"))
# print("El area de un triangulo es ",(1/2 * (base*altura)))


# Convertir la cantidad de dólares ingresados por un usuario
# a pesos colombianos y mostrar el resultado en pantalla.

# un_dolar= 4068.96
# dolares = float(input("dame dolares $\n"))
# print(dolares," $ = ",((dolares*un_dolar)/1),"pesos colombianos")

# Convertir los grados centígrados ingresados por un usuario
# a grados Fahrenheit y mostrar el resultado en pantalla.

# grados_centigrados= float(input("dame los grados centigrados\n"))
# grados_fahrenheit= ((grados_centigrados * 9)/5) + 32
# print(grados_centigrados, " grados centigrados = ", grados_fahrenheit)

# Mostrar en pantalla la cantidad de segundos que tiene un lustro.

# lustro = float(input("dime cuantos lustros\n"))
# print(lustro, " lustro = ", (1.577e+8*lustro), " segundos")

# Calcular la cantidad de segundos que le toma a la luz viajar
# del sol a Marte y mostrar el resultado en pantalla.

# velocidad_luz_1s_km = 299792.458
# distacia_marte_sol_km = 227940000
# print("la velocidad luz tarda ",int(distacia_marte_sol_km/velocidad_luz_1s_km), "segundos")

# Calcular el número de vueltas que da una llanta en 1 km,
# dado que el diámetro de la llanta es de 50 cm, mostrar el resultado en pantalla.

# una_vuelta_en_metros=int(2*3.1416*25)/100
# print("da", 1000/una_vuelta_en_metros, "vueltas")

# Calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros de altura
# cuando el ángulo que forman los rayos del sol con el suelo es de 22º.
# import math
#
# metros_edificio= 20
# angulo=22
# print("la longitud de la sombra es de",metros_edificio/math.tan(angulo))

# Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma.

# edad1 = int(input("dame la primera edad\n"))
# edad2 = int(input("dame la segunda edad\n"))
#
# print("Son iguales" if (edad1 == edad2) else "No son iguales")

#Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.\

# from datetime import datetime, timedelta
#
# fecha_nacimiento = datetime(1995, 10, 23, 00, 00, 00)
# fecha_ahora= datetime.utcnow() + timedelta(hours=1)
# meses= (fecha_ahora - fecha_nacimiento)/30.417
#
# print(meses.days, "meses")

#Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias
# (Español, Matemáticas, Economía, Programación, Ingles).
resultado= (5+6+5+7+6)/5
print(resultado)