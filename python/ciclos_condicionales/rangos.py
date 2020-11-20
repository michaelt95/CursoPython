# for valor in range(-1, 11):
#     print(valor)

# for valor in range(0, 101, 2):
#     print(valor)

lista = [1,2,3,4,5]

# for indice in range(len(lista)):
#     print("Indice:", indice, "valor:", lista[indice])

# for indice, valor in enumerate(lista):
#     print("Indice:", indice, "valor:", valor)

for indice, valor in enumerate(lista, 10):
    print("Indice:", indice, "valor:", valor)