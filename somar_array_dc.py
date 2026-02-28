# mesma função de soma, mas com divisão e conquista
def somar(lista):
    n = len(lista)

    if n == 1:
        return lista[0]

    meio = n//2
    l = somar(lista[:meio])
    r = somar(lista[meio:])

    return l + r

lista = [2, 4, 6]

print(somar(lista))
