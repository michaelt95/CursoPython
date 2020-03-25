class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

    def comun(self):
        print("Este es un metodo de Animal")


class Mascota:

    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print("Este es un metodo de Mascota")


class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrad(self):
        print("Ladrando")

    def comun(self):
        print("Este es un metodo de Perro")


class Gato(Animal):

    def ronronear(self):
        print("Ronroneo")


firulais = Perro("Firulais")
firulais.comun()
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_de_adopcion)

# El metodo en comun busca la clase principal y despues de izquierda a derecha en las clases que hereda
