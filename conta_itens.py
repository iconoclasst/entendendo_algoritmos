# Contar itens de lista com recursão

def conta(lista):
    ctt=1
    if len(lista)==0:
        return 0

    lista.pop(0)

    return ctt + conta(lista)

lista = [1,2,3,4,5,6,7]

print(conta(lista))

# Contar itens com divisão e conquista

def contadc(lista):
    if len(lista)==0:
        return 0
    if len(lista)==1:
        return 1

    meio = len(lista)//2
    esquerda = contadc(lista[:meio])
    direita = contadc(lista[meio:])

    return esquerda + direita

lista = [1,2,3,4,5,6,7]
print(contadc(lista))
