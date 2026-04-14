vertices = {}

vertices['a'] = ['b', 'd']
vertices['b'] = ['d']
vertices['c'] = ['a', 'd']
vertices['d'] = ['c']

print("Grafo G: ")
print(vertices)
gt = {}
for u in vertices:
    gt[u] = []

for k, v in vertices.items():
    for i in v:
        gt[i].append(k)

print("Transposta de G: ")
print(gt)
    

    # print("O vértice {} tem aresta com {}".format(v, vertices[v]))