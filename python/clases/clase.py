class Usuario:

    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saluda(self):
        return "Hola, soy un usuario " + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)


# codi = Usuario()
# codi.username = "codi"  # generar atributos fuera de la clase
# codi.correo = "codi@gmail.com"  # generar atributos fuera de la clase
# print(type(codi))  # tipo de clase

codi = Usuario("Codi", "codi@codigofacilito.com","Codigo")
facilito = Usuario()

resultado = codi.saluda()
print(resultado)

print("pene " + str(3))