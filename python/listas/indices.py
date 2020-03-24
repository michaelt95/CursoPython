# Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.
# [:] Todos los elementos.
# [start:] Todos los elementos desde el índice establecido(start).
# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
# [start:end] Todos los elementos de un rango de índices.
# [start:end:step] Todos los elementos de un rango de índices con saltos.
# De igual forma, este listado es aplicable a las tuplas y los strings.
cursos = ["python","django","flask","c","c++","c#","java","php"]

sub = cursos[::]

print(sub)