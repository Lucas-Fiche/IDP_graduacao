def calcular_gastos_feira():
    quantidade_casos = int(input().strip())
    resultados = []

    for _ in range(quantidade_casos):
        quantidade_produtos = int(input().strip())
        produtos_preco = {}

        for _ in range(quantidade_produtos):
            linha = input().rsplit(' ', 1)
            nome = linha[0].strip()
            preco = float(linha[1].strip())
            produtos_preco[nome] = preco

        quantidade_compras = int(input().strip())
        total = 0.0

        for _ in range(quantidade_compras):
            linha = input().rsplit(' ', 1)
            nome = linha[0].strip()
            quantidade = int(linha[1].strip())
            total += produtos_preco.get(nome, 0) * quantidade

        resultados.append(f"R$ {total:.2f}")

    print("\n".join(resultados))

calcular_gastos_feira()
