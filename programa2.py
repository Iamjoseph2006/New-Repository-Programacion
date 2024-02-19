def ordenar_fila(matriz, indice_fila):
    matriz[indice_fila] = sorted(matriz[indice_fila])

# Matriz de ejemplo
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

indice_fila_a_ordenar = 1
print("Matriz original:")
for fila in matriz:
    print(fila)

ordenar_fila(matriz, indice_fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
