# Formas de representar grafos
## Uma matriz N*N em que N são os vértices. Se houver uma aresta incidente a posição mat[n1][n1], o valor é 1. Se não, o valor é 0.


# Exemplo
## Vertices = [1, 2, 3, 4]
## Arestas = [{1,2}, {2,3}, {1,3}, {3,4}, {2, 4}]

import numpy as np

matriz = np.zeros((5,5), dtype=int)

for i in range(0, 4):
    matriz[0][i+1] = i+1
    matriz[i+1][0] = i+1

print("Grafo vazio:")
print(matriz)

# Criar arestas
matriz[1][2] = 1
matriz[2][3] = 1
matriz[1][3] = 1
matriz[3][4] = 1
matriz[2][4] = 1

print("Grafo e suas arestas:")
print(matriz)