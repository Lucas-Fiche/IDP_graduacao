vertices, arestas = map(int, input().split())
grafo = [[0] * vertices for i in range(vertices)]

for i in range(arestas):
    vertice_u, vertice_v = map(int, input().split())
    grafo[vertice_u-1][vertice_v-1] = 1
    grafo[vertice_v-1][vertice_u-1] = 1

for linha in grafo:
    print(" ".join(map(str, linha)))
