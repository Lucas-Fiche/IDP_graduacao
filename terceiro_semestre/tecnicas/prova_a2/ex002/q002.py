def solucao():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        grafo[a].append(b)
        grafo[b].append(a)
    
    pos_ben, pos_animal, pos_saida = map(int, input().split())
    
    def bfs(inicio):
        distancia = [-1] * (n+1)
        distancia[inicio] = 0
        fila = [inicio]
        posicao = 0
        
        while posicao < len(fila):
            atual = fila[posicao]
            posicao += 1
            for proximo in grafo[atual]:
                if distancia[proximo] == -1:
                    distancia[proximo] = distancia[atual] + 1
                    fila.append(proximo)
        return distancia
    
    distancia_ben = bfs(pos_ben)
    distancia_animal = bfs(pos_animal)
    
    if distancia_ben[pos_saida] == -1 or distancia_animal[pos_saida] == -1:
        return "FUGA" if distancia_ben[pos_saida] != -1 else "EMBATE"
    
    return "FUGA" if distancia_ben[pos_saida] < distancia_animal[pos_saida] else "EMBATE"

print(solucao())
