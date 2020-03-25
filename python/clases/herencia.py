class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")


class Perro(Animal,):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrad(self):
        print("Ladrando")


class Gato(Animal):

    def ronronear(self):
        print("Ronroneo")


firulais = Perro("Firulais")
firulais.ladrad()
firulais.comer()
firulais.dormir()

bola_de_nieve = Gato()
bola_de_nieve.comer()
bola_de_nieve.dormir()
