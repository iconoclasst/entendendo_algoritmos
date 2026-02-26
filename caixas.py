import random


# Problema das caixas com recursão
# A chave (bit 1) pode estar em qualquer caixa
# Usamos recursão para abrir as caixas e verificar

caixas = {}
for i in range(10):
    caixas[i] = random.choices([0,1], weights=[0.9, 0.1])[0]

def achar_chave(caixas, indice=0):
    if indice >= len(caixas):
        return None

    if caixas[indice] == 1:
        return indice

    return achar_chave(caixas, indice+1)


a= achar_chave(caixas)
print(a)

print(caixas)
