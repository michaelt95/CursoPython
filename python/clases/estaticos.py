class Triangulo:

    numero = 2
    # No se puede instanciar si tiene metodos staticos

    @staticmethod
    def area(base, altura):
        return (base * altura) / Triangulo.numero


resultado = Triangulo.area(10, 20)
print(resultado)