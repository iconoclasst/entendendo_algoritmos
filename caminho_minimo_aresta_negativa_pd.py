    


def cmc(grafo, t):
    ncols = len(grafo)

    opt = [[0 for _ in range(ncols)] for _ in range(ncols)]

    for v in grafo:
        opt[0][v-1] = float('inf')
    opt[0][t-1] = 0

    for i in range(1, ncols):
        for v in grafo:
            opt[i][v-1] = opt[i-1][v-1]
        for v in grafo:
            for w, l in grafo[v]:
                opt[i][v-1] = min(opt[i][v-1], opt[i-1][w-1]+l)

    print("Tabela final: ")
    for l in opt:
        print(l)

    linha_otima = opt[2]
    print()
    print("Solução ótima: ")
    for i in range(len(linha_otima)):
        print(f"OPT({i+1}) = {linha_otima[i]}")
    

grafo = {
    1:[(4, 2), (2, -4)],
    2:[(3, 2)],
    3:[(4, 5)],
    4:[]
}

t = 4

cmc(grafo, t)


