def calcular_tabela_hash(num_enderecos, num_chaves, chaves):
    tabela_hash = [[] for _ in range(num_enderecos)]

    for chave in chaves:
        indice = chave % num_enderecos
        tabela_hash[indice].append(chave)

    for i in range(num_enderecos):
        print(f"{i} -> ", end="")
        for chave in tabela_hash[i]:
            print(f"{chave} -> ", end="")
        print("\\")

num_enderecos, num_chaves = map(int, input().split())
chaves = list(map(int, input().split()))

calcular_tabela_hash(num_enderecos, num_chaves, chaves)
