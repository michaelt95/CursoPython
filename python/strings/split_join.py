lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separador = ";"

resultado = lenguajes.split(separador)  #es una lista
print(resultado)
nuevo_string = separador.join(resultado)
print(nuevo_string)
texto = """"Este es un texto
con
saltos
de

linea"""

resultado = texto.splitlines()

print(resultado)
