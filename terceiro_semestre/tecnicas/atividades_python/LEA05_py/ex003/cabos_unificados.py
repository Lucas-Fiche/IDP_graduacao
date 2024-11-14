import heapq

def custo_minimo_conexao(num_cabos, comprimentos):
    heapq.heapify(comprimentos)
    custo_total = 0

    while len(comprimentos) > 1:
        menor1 = heapq.heappop(comprimentos)
        menor2 = heapq.heappop(comprimentos)
        
        custo_total += menor2
        custo_conexao = menor1 + menor2

        heapq.heappush(comprimentos, custo_conexao)
    
    return custo_total

num_cabos = int(input())
comprimentos = list(map(int, input().split()))

resultado = custo_minimo_conexao(num_cabos, comprimentos)
print(resultado)
