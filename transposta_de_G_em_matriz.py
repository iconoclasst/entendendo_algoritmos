import numpy as np

matriz = np.zeros((5,5), dtype=int)

for i in range(0, 4):
    matriz[0][i+1] = i+1
    matriz[i+1][0] = i+1

# print("Grafo vazio:")
# print(matriz)

matriz[1][2] = 1
matriz[2][3] = 1
matriz[1][3] = 1
matriz[3][4] = 1
matriz[2][4] = 1

print("Grafo e suas arestas antes:")
print(matriz)
n = 5

tp = matriz.copy()

# print(tp)

for i in range(1, n):
    for j in range(1, n):
        if matriz[i][j] == 1:
            tp[i][j] = 0
            tp[j][i] = 1
            

print("Grafo e suas arestas depois:")
print(tp)

