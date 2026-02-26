
# Problema simples de recursão

def contagem(i):
    if i<=0:
        print("fim")
        return 
    print(i)
    contagem(i-1)

i=10
contagem(i)
