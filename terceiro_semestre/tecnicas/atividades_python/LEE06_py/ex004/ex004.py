def calcular_menor_caminho(numero_ilhas, conexoes, origem, destino):
    grafo = {ilha: [] for ilha in range(1, numero_ilhas + 1)}
    for ilha_a, ilha_b in conexoes:
        grafo[ilha_a].append(ilha_b)
        grafo[ilha_b].append(ilha_a)
    
    distancias = [-1] * (numero_ilhas + 1)
    fila_exploracao = [origem]
    distancias[origem] = 0

    while fila_exploracao:
        ilha_atual = fila_exploracao.pop(0)
        for vizinha in grafo[ilha_atual]:
            if distancias[vizinha] == -1:
                distancias[vizinha] = distancias[ilha_atual] + 1
                fila_exploracao.append(vizinha)
                if vizinha == destino:
                    return distancias[vizinha]

    return -1

def main():
    parametros = input().split()
    numero_ilhas, numero_conexoes = int(parametros[0]), int(parametros[1])
    conexoes = [tuple(map(int, input().split())) for _ in range(numero_conexoes)]
    menor_caminho = calcular_menor_caminho(numero_ilhas, conexoes, 1, numero_ilhas)
    print(menor_caminho)

if __name__ == "__main__":
    main()
