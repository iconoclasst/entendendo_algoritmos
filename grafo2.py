# Formas de representar grafos
## Um mapa de N vértices, e em cada chave desse arranjo, o valor é uma lista ligada com os outros vértices no qual aquele índice tem uma aresta

# Exemplo
## Vertices = [1, 2, 3, 4]
## Arestas = [{1,2}, {2,3}, {1,3}, {3,4}, {2, 4}]

# O primeiro vértice é um, e tem arestas com os vértices 2 e 3
vertices = {}

vertices[1] = [2, 3]
vertices[2] = [1, 3, 4]
vertices[3] = [1, 2, 4]
vertices[4] = [2, 3]

for v in vertices:
    print("O vértice {} tem aresta com {}".format(v, vertices[v]))