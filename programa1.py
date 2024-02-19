def buscar_valor(matriz, valor):
    """
    Función que busca un valor específico en una matriz bidimensional.

    :param matriz: La matriz bidimensional en la que se va a realizar la búsqueda.
    :param valor: El valor que se va a buscar en la matriz.
    :return: True si se encuentra el valor en la matriz, False de lo contrario.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"El valor {valor} se encontró en la posición ({i}, {j}) de la matriz.")
                return True
    print(f"El valor {valor} no se encontró en la matriz.")
    return False

# Matriz de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Llamada a la función buscar_valor
buscar_valor(matriz, valor_a_buscar)