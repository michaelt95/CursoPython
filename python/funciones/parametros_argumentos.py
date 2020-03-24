def crear_usuario(nombre, apellido, edad=24):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }


codi = crear_usuario(nombre="Michael", apellido="Torres")
# codi = crear_usuario("Michael", "Torres")

for index in codi:
    print(index, "=", codi[index])
