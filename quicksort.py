# algoritmo de ordenação quicksort com dc

def quicksort(lista):
    n = len(lista)

    if n < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

lista = [10, 5, 3, 2, 11, 2]

print(quicksort(lista))
