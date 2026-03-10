

#entrada: arranjo A[a1, a2, ..., an]
#saida: permutacao de arranjo A tal que a1 <= a2 <= a3 ... <= an

def ordenacao_insercao(arranjo):
    n = len(arranjo)

    for j in range(1, n+1):
        chave = arranjo[j]
        i = j-1
        while i > 0 and arranjo[i] > chave:
            arranjo[i+1] = arranjo[i]
            i += 1
        arranjo[i+1]=chave
    return arranjo

arranjo = [5,2,4,6,1,3]

print(arranjo)
print(ordenacao_insercao(arranjo))
