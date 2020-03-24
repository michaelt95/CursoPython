# def saluda():
#     print("Hola mundo!")
#
# saluda()

def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de python 3".format(nombre)


def suma(val1, val2, val3):
    return val1+val2+val3

def obtener_curso():
    return "Curso de Python", "Basico", 3.6

print(crear_mensaje("Michael"))

print(suma(10, 20, 30))

curso,nivel,version = obtener_curso()
print(curso,nivel,version)