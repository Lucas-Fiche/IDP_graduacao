def main():
    import sys
    input = sys.stdin.read
    dados = input().strip().split("\n")

    T = int(dados[0])
    index = 1
    resultados = []

    for _ in range(T):
        M, N = map(int, dados[index].split())
        index += 1

        dicionario = {}
        for _ in range(M):
            palavra_japonesa = dados[index]
            palavra_portuguesa = dados[index + 1]
            dicionario[palavra_japonesa] = palavra_portuguesa
            index += 2

        letras_traduzidas = []
        for _ in range(N):
            linha = dados[index]
            index += 1
            palavras = linha.split()
            linha_traduzida = " ".join(
                dicionario.get(palavra, palavra) for palavra in palavras
            )
            letras_traduzidas.append(linha_traduzida)

        resultados.append("\n".join(letras_traduzidas))

    print("\n\n".join(resultados))


if __name__ == "__main__":
    main()
