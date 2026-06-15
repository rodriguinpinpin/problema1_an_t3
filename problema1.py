laberinto = [
    ["F", 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    ["I", 1, -1, 1, 1, 1, 0, 1, 1]
]

filas = 9
columnas = 9

camino = [[0] * columnas for _ in range(filas)]
inicio_fila = 8
inicio_columna = 0
fin_fila = 0
fin_columna = 0

def obtener_vidas(valor):
    if valor == -1:
        return 1
    elif valor == -2:
        return 2
    return 0
