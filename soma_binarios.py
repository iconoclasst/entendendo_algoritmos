# Dados dois arranjos A e B com n elementos, gerar um arranjo C com n+1 elementos com os resultados binários

#pseudocódigo:
#  n = A.size + 1
#  aux = 0
#  for j=0 to n-1:
#     soma = A[j] + B[j] + aux
#     C[j] = (soma % 2)
#     aux = soma // 2
#
#  C[n] = aux
#  return C
#

def soma_binarios(A, B):
    n = len(A)
    aux = 0
    C = []
    for j in range(n):
        soma = A[j] + B[j] + aux
        C.append(soma % 2)
        aux = soma // 2

    C.append(aux)
    return C


a = [1, 0, 0, 1]
b = [1, 1, 0, 0]
# resultado: C = [00110]

print("resultado esperado: C = [00110]")
print(soma_binarios(a, b))

