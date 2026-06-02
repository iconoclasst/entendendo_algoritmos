moedas = [100, 25, 10, 5, 1]

valor = 289

i=0

solucao = []

while True:
    if valor <= 0:
        break
    if moedas[i] <= valor:
        solucao.append(moedas[i])
        valor -= moedas[i]
    else:
        i += 1

print(solucao)

    
