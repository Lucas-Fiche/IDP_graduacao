def organizar_listas():
    quantidade = int(input())
    resultados = []

    for _ in range(quantidade):
        linha = input()
        itens = sorted(set(linha.split()))
        resultados.append(" ".join(itens))

    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    organizar_listas()
