def obter_cartas_repetidas(baralho1, baralho2):
    cartas_marcadas = set(baralho1)
    cartas_repetidas = {carta for carta in baralho2 if carta in cartas_marcadas}
    return ''.join(sorted(cartas_repetidas))

def analisar_duelos(quantidade_duelos, lista_baralhos):
    resultados = []
    
    for baralho1, baralho2 in lista_baralhos:
        cartas_repetidas = obter_cartas_repetidas(baralho1, baralho2)
        
        if cartas_repetidas:
            resultados.append(cartas_repetidas)
        else:
            resultados.append("Baralhos prontos para o duelo")
    
    return resultados

quantidade_duelos = int(input())
lista_baralhos = [input().split() for _ in range(quantidade_duelos)]

resultados = analisar_duelos(quantidade_duelos, lista_baralhos)
for resultado in resultados:
    print(resultado)
