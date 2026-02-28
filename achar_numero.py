# retornar True se achar numero usando dc

def achar(lista, value):
    n = len(lista)

    if n==0:
        return False

    if n==1:
        return lista[0]==value

    meio = n//2
    l = achar(lista[:meio], value)
    r = achar(lista[meio:], value)
    
    return l or r

i = 3
lista = [1, 2, 2, 4, 5]

print(achar(lista, i))

