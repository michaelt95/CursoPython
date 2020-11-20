def suma(parametro_requerido, *args):
    total = 0
    print(parametro_requerido)
    # print(args) es una tupla
    for valor in args:
        total += valor
    return total


def usuarios_autenticados(**kwargs):
    # lo covierte en un diccionario con el atributo como key
    print(kwargs)


resultado = suma("Este es un argumento requerido", 10, 20, 30)
print(resultado)

usuarios_autenticados(codi=True, facilito=False)

def combinacion(requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)


combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)
