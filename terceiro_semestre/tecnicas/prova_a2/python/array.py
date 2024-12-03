def calcular_valor_hash(linha, indice_elemento):
    valor_hash = 0
    for indice_caractere, caractere in enumerate(linha):
        posicao_no_alfabeto = ord(caractere) - ord('A')
        valor_hash += posicao_no_alfabeto + indice_elemento + indice_caractere
    return valor_hash

def principal():
    numero_de_casos_teste = int(input())
    resultados = []
    for _ in range(numero_de_casos_teste):
        quantidade_linhas = int(input())
        hash_total = 0
        for i in range(quantidade_linhas):
            linha = input().strip()
            hash_total += calcular_valor_hash(linha, i)
        resultados.append(hash_total)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    principal()
