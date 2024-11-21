import heapq

def encontrar_caminho_minimo(mapa, origem, destino):
    distancias = {local: float('inf') for local in mapa}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, local_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[local_atual]:
            continue

        for vizinho, custo in mapa[local_atual]:
            nova_distancia = distancia_atual + custo

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias[destino]

def resolver_problema():
    locais, rotas = map(int, input().split())
    mapa_cidades = {i: [] for i in range(1, locais + 1)}

    for _ in range(rotas):
        ponto_a, ponto_b, distancia = map(int, input().split())
        mapa_cidades[ponto_a].append((ponto_b, distancia))
        mapa_cidades[ponto_b].append((ponto_a, distancia))

    ponto_partida = 1
    ponto_chegada = locais

    menor_distancia = encontrar_caminho_minimo(mapa_cidades, ponto_partida, ponto_chegada)

    if menor_distancia == float('inf'):
        print("Preso no IDP")
    else:
        print(f"Distancia para chegar em casa: {menor_distancia}")

if __name__ == "__main__":
    resolver_problema()
