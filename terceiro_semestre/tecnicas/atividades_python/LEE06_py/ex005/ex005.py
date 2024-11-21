def calcular_menor_caminho(pontos, caminhos, pos_agente, pos_extintor, pos_incendio):
    grafo = {i: [] for i in range(1, pontos + 1)}
    for origem, destino in caminhos:
        grafo[origem].append(destino)
        grafo[destino].append(origem)

    def busca_menor_caminho(inicio, objetivo):
        distancias = [-1] * (pontos + 1)
        fila_explorar = [inicio]
        distancias[inicio] = 0

        while fila_explorar:
            atual = fila_explorar.pop(0)
            if atual == objetivo:
                return distancias[atual]
            for vizinho in grafo[atual]:
                if distancias[vizinho] == -1:
                    distancias[vizinho] = distancias[atual] + 1
                    fila_explorar.append(vizinho)
        return -1

    caminho_agente_extintor = busca_menor_caminho(pos_agente, pos_extintor)
    caminho_extintor_incendio = busca_menor_caminho(pos_extintor, pos_incendio)

    return caminho_agente_extintor + caminho_extintor_incendio

def main():
    dados_iniciais = input().split()
    total_pontos, total_caminhos = int(dados_iniciais[0]), int(dados_iniciais[1])
    conexoes = [tuple(map(int, input().split())) for _ in range(total_caminhos)]
    posicoes = list(map(int, input().split()))
    agente, extintor, incendio = posicoes[0], posicoes[1], posicoes[2]
    resultado = calcular_menor_caminho(total_pontos, conexoes, agente, extintor, incendio)
    print(resultado)

if __name__ == "__main__":
    main()
