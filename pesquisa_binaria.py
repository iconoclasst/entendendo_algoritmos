
def pesquisa_binaria(array, item):
    # Range do array
    baixo=0
    alto = len(array)-1
    
    while baixo <= alto:
        meio = (baixo+alto)//2
        chute = array[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

a = [1,2,3,4,5,6,7,8,9,10]
i = 6
r = pesquisa_binaria(a,i)
print(r)

