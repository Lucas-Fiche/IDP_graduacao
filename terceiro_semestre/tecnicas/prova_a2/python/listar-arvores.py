def main():
    import sys
    from collections import defaultdict

    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")

    T = int(dados[0])
    index = 1
    resultados = []

    for t in range(T):
        especies = defaultdict(int)
        total = 0

        while index < len(dados) and not dados[index].strip():
            index += 1

        while index < len(dados) and dados[index].strip():
            especie = dados[index].strip()
            especies[especie] += 1
            total += 1
            index += 1

        especies_ordenadas = sorted(especies.keys())
        resultado_atual = []

        for especie in especies_ordenadas:
            percentual = (especies[especie] * 100) / total
            resultado_atual.append(f"{especie} {percentual:.4f}")

        resultados.append("\n".join(resultado_atual))

    print("\n\n".join(resultados))


if __name__ == "__main__":
    main()
