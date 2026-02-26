
def buscamenor(array):
    mval = array[0]
    mind = 0
    for i in range(1, len(array)):
        if mval < array[i]:
            mval = array[i]
            mind = i
    return mind

def ordenacaoselecao(array):
    narray = []
    for i in range(len(array)):
        menor = buscamenor(array))
        narray.append(array.pop(menor))

    return narray

# Ordenação por seleção
# Complexidade O(NxN)
# Tirar o menor valor do array e passar pra outro
# até que não sobre mais. 

