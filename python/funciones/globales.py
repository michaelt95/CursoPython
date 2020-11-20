animal = "Leon"  #variable globales

def mostrar_animal():
    global animal  #para hacerla global
    animal = "Ballena"  #variable locales
    print(animal)


mostrar_animal()
print(animal)