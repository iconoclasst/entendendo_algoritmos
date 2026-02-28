# Somar elementos de array com recursão

def soma(array):
    #caso base
    if len(array)==0:
        return 0

    #Recursão
    value = array[0]
    array.pop(0)
    return value + soma(array)


print(soma([2,4,6]))
