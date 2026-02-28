# achar menor valor usando dc

def minimo(lista):
    n = len(lista)

    if n==1:
        return lista[0]

    m = n//2
    l = minimo(lista[:m])
    r = minimo(lista[m:])

    if l < r:
        return l
    else:
        return r

lista = [44, 22, 1, 54, 2, -3]
print(minimo(lista))

