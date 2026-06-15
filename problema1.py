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

def resolver(fila, columna, vidas):

    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        return False

    if camino[fila][columna] == 1:
        return False

    if laberinto[fila][columna] == 0:
        return False

    vidas_restantes = vidas - obtener_vidas(laberinto[fila][columna])

    if vidas_restantes <= 0:
        return False
    
    camino[fila][columna] = 1

    print("Posición:", fila, columna, "Vidas:", vidas_restantes)

    if fila == fin_fila and columna == fin_columna:
        return True

    if resolver(fila + 1, columna, vidas_restantes):
        return True

    if resolver(fila, columna + 1, vidas_restantes):
        return True

    if resolver(fila - 1, columna, vidas_restantes):
        return True

    if resolver(fila, columna - 1, vidas_restantes):
        return True

    camino[fila][columna] = 0
    return False
