def main():
    n = int(input())
    grafo = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        dados = list(map(int, input().split()))
        total = dados[0]
        conectados = dados[1:]
        for conexao in conectados:
            grafo[i][conexao - 1] = 1

    for linha in grafo:
        print(" ".join(map(str, linha)))


if __name__ == "__main__":
    main()