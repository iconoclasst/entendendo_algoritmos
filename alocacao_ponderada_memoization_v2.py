def computar_p(tarefas):
    def compativel(t1, t2):
        if t1[1] <= t2[0]:
            return True
        return False

    p = []

    for j in range(len(tarefas)):
        ultimo = 0

        for i in range(j-1, -1, -1):
            if compativel(tarefas[i], tarefas[j]):
                ultimo = i+1
                break
        p.append(ultimo)
    return p

def fb(n, tarefas):
    p = computar_p(tarefas)

    m = {}
    m[0] = 0

    def computar_opt(j):
        if j not in m:
            m[j] = max(computar_opt(j-1), tarefas[j-1][2] + computar_opt(p[j-1]))
        return m[j]
    valor = computar_opt(n)

    s = []

    def solucao(j):
        if j == 0:
            return 
        peso = tarefas[j-1][2]
        if peso + m[p[j-1]] > m[j-1]:
            s.append(tarefas[j-1])
            solucao(p[j-1])
        else:
            solucao(j-1)
        solucao(n)
        s.reverse()
    
    return valor, s

tarefas = [(1, 3, 4), (2, 5, 12), (2, 4, 3), (7, 12, 3), (8, 14, 15)]
tarefas = sorted(tarefas, key=lambda x: x[1 ])
n = len(tarefas)

print(fb(n, tarefas))
