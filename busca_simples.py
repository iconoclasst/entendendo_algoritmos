#busca simples em array
import random

array = []

for i in range(1000):
    array.append(random.randint(1, 100))


valor = 99

try:
    ctt=1
    for i in array:
        if valor == i:
            print(f"Valor encontrado após {ctt} tentativas")
            break
        else:
            ctt+=1
except:
    print(f"valor {valor} não encontrado")

order_array = set(array)

try:
    ctt=1
    for i in order_array:
        if valor == i:
            print(f"Valor encontrado após {ctt} tentativas")
            break
        else:
            ctt+=1
except:
    print(f"valor {valor} não encontrado")


