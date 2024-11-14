def busca_par(num, alvo, lista):
    checados = set()
    for valor in lista:
        restante = alvo - valor
        if restante in checados:
            return f"{min(restante, valor)} {max(restante, valor)}"
        checados.add(valor)
    return "Nao existe"

num, alvo = map(int, input().split())
lista = list(map(int, input().split()))

print(busca_par(num, alvo, lista))
