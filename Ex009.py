#Ex009: Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz.
#([[3, 4, 1], [3, 1, 5]])


import numpy as np

matriz = np.array ([[3, 4, 1],
                   [3, 1, 5]])

somar_matriz = 0
for linha in range(matriz.shape[0]):
  for coluna in range(matriz.shape[1]):
    somar_matriz += matriz[linha][coluna]
print(f"A soma de todos elementos da matriz é: {somar_matriz}")
