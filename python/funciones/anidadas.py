def comenzar_play_list(lista):

    def reproducir():
        nonlocal lista  # nonlocal con variables que se encuentren en ciclos, condiciones, funciones . . .
        lista = [1, 2, 3]
        for val in lista:
            print(val)

    reproducir()
    print(lista)


lista = ["Track1", "Track2", "Track3", "Track4"]
comenzar_play_list(lista)