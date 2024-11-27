def main():
    from collections import defaultdict

    N, M = map(int, input().split())

    lista = defaultdict(list)

    for _ in range(M):
        U, V = map(int, input().split())
        lista[U].append(V)
        lista[V].append(U)

    noVisitado = [False] * (N + 1)

    def dfs(no):
        pilha = [no]
        noVisitado[no] = True

        while pilha:
            u = pilha.pop()
            for v in lista[u]:
                if not noVisitado[v]:
                    noVisitado[v] = True
                    pilha.append(v)

    gangues = 0

    for i in range(1, N + 1):
        if not noVisitado[i]:
            dfs(i)
            gangues += 1

    print(f"{gangues} gangue(s) no clube da briga")

if __name__ == "__main__":
    main()


