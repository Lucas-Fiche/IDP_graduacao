import heapq
from math import inf
from collections import defaultdict

def algoritmo_dijkstra(inicio, nos, grafo, bloqueados):
    distancias = [inf] * (nos + 1)
    distancias[inicio] = 0

    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))

    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[no_atual]:
            continue

        for vizinho, peso in grafo[no_atual]:
            if vizinho in bloqueados:
                continue
            if distancias[no_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[no_atual] + peso
                heapq.heappush(fila_prioridade, (distancias[vizinho], vizinho))
    
    return distancias

def main():
    nos, arestas, cameras = map(int, input().split())

    bloqueados = set()
    for _ in range(cameras):
        cam = int(input())
        bloqueados.add(cam)

    grafo = defaultdict(list)
    for _ in range(arestas):
        u, v = map(int, input().split())
        grafo[u].append((v, 1))
        grafo[v].append((u, 1))

    patio, saida, chave = map(int, input().split())

    dist_patio_bloqueado = algoritmo_dijkstra(patio, nos, grafo, bloqueados)
    dist_chave_bloqueado = algoritmo_dijkstra(chave, nos, grafo, bloqueados)

    if dist_patio_bloqueado[chave] == inf or dist_chave_bloqueado[patio] == inf:
        print("impossivel fugir")
        return

    ida_e_volta_chave = dist_patio_bloqueado[chave] + dist_chave_bloqueado[patio]

    dist_patio_livre = algoritmo_dijkstra(patio, nos, grafo, set())

    if dist_patio_livre[saida] == inf:
        print("impossivel fugir")
        return

    para_saida = dist_patio_livre[saida]

    print(ida_e_volta_chave, para_saida)

if __name__ == "__main__":
    main()
