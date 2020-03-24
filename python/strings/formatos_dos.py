curso = "Python"
version = 3

# resultado = "Curso de %s %d" %(curso, version)
# resultado = "Curso de {} {}".format(curso, version)
# resultado = "Curso de {a} {b}".format(a=curso, b=version)
resultado = "Curso de {a} {b}".format(b=version, a=curso)
print(resultado)