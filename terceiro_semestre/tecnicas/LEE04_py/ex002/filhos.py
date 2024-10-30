def filho_esquerdo(n):
    return 2 * n

def filho_direito(n):
    return 2 * n + 1

def main():
    n, c = map(int, input().split())

    arvore = [-1] * (n + 1)
    valores = list(map(int, input().split()))
    for i in range(1, n + 1):
        arvore[i] = valores[i - 1]

    for _ in range(c):
        no_consulta = int(input())

        if arvore[1] == -1:
            print("NULL")
            break

        esquerdo = filho_esquerdo(no_consulta)
        direito = filho_direito(no_consulta)

        if esquerdo <= n and arvore[esquerdo] != -1:
            print(arvore[esquerdo], end=" ")
        else:
            print("NULL", end=" ")

        if direito <= n and arvore[direito] != -1:
            print(arvore[direito])
        else:
            print("NULL")

if __name__ == "__main__":
    main()
