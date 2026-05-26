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

    for j in range(1, n+1):
        m[j] = max(m[j-1], tarefas[j-1][2] + m[p[j-1]])

    return m[n]


tarefas = [(1, 3, 4), (2, 5, 12), (2, 4, 3), (7, 12, 3), (8, 14, 15)]
tarefas = sorted(tarefas, key=lambda x: x[1 ])
n = len(tarefas)

print(fb(n, tarefas))
