diccionario = {"a":1, "b":2, "c":3, "a":4}

# resultado = diccionario["a"]
# resultado = "a" in diccionario
# resultado = diccionario.get("a")
# resultado = diccionario.get("z", "La llave no existe")
resultado = diccionario.setdefault("z", {})

print(resultado)
print(diccionario)