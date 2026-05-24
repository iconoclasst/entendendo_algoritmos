
def alocacao_gulosa(n, t):
    S = []

    jl = 0

    for i, j in t:
        if i >= jl and j <= n:
            S.append((i, j))
            jl = j

    return S
        
t = [(4, 20), (2, 14), (15, 17)]
n = 30

t = sorted(t, key=lambda x: x[1])

print(alocacao_gulosa(n, t))
