A = int(input().strip())

lista_churrasco = set()

for i in range(A):
    P = int(input().strip())
    
    for i in range(P):
        produto = input().strip()
        if produto in lista_churrasco:
            print(f"{produto} ja tem")
        else:
            print(f"adicionando {produto}")
            lista_churrasco.add(produto)

print("Itens do churrasco:")
for produto in sorted(lista_churrasco):
    print(produto)
