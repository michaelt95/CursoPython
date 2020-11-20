# tupla = (1, 2, 3, 4)
# uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]
# uno, dos, tres, cuatro = tupla
#con el * crea un array al final
tupla = (1, 2, 3, 4, 5, 6)
#1 forma
# uno, dos, tres, *cuatro = tupla
# print(uno)
# print(dos)
# print(tres)
# print(cuatro)
#2 forma
# uno, *dos, cinco, seis = tupla
# print(uno)
# print(dos)
# print(cinco)
# print(seis)

#duplas con listas
lista = [10, 20, 30, 40]
tupla_dos = (100, 200, 300, 400)

resultado = zip(tupla, lista,tupla_dos)
# resultado = tuple(resultado)
resultado = list(resultado)
print(resultado)