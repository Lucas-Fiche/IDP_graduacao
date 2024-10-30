import bisect

def promocao_cinema(P, R, lista_cadeiras):
    cadeiras_ordenadas = []
    lista_resultados = []
    
    for cadeira_atual in lista_cadeiras:
        bisect.insort(cadeiras_ordenadas, cadeira_atual)
        
        if R <= len(cadeiras_ordenadas):
            cadeira_vencedora = cadeiras_ordenadas[R - 1]
        else:
            cadeira_vencedora = cadeiras_ordenadas[-1]
        
        lista_resultados.append(cadeira_vencedora)
    
    return lista_resultados

P, R = map(int, input().split())
lista_cadeiras = list(map(int, input().split()))

lista_resultados = promocao_cinema(P, R, lista_cadeiras)
for resultado_atual in lista_resultados:
    print(resultado_atual)
