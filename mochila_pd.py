itens = [(2, 1), (3, 2), (7, 4), (8,5)]

capacidade = 5

opt = [[0 for _ in range(capacidade+1)] for _ in range(len(itens)+1)]

for i in range(1, len(itens)+1):
    for w in range(capacidade+1):
        if itens[i-1][1] > w:
            opt[i][w] = opt[i-1][w]
        else:
            opt[i][w] = max(opt[i-1][w], itens[i-1][0] + opt[i-1][w-itens[i-1][1]])

for l in opt:
    print(l)

optmax = max(max(l) for l in opt)

print(optmax)
