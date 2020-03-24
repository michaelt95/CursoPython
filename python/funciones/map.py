# En Python, la función map nos permite aplicar una función sobre los items
# de un objeto iterable (lista, tupla, etc...).
# Sintaxis
# map(function, objeto iterable)

# def cuadrado(numero):
#     return numero * numero
#
#
# lista = [1, 2, 3, 4, 5]
# resultado = map(cuadrado, lista)
#
# lista_resultado = list(resultado)
# print(lista_resultado)

# funcion lambda

lista = [1, 2, 3, 4, 5]
resultado = map(lambda numero: numero * numero, lista)

lista_resultado = list(resultado)
print(lista_resultado)
