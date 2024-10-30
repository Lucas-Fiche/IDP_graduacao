import sys

def counting_sort_notas(lista, max_valor=10):
    contagem = [0] * (max_valor + 1)
    for nota in lista:
        contagem[nota] += 1

    saida = []
    for nota in range(max_valor + 1):
        saida.extend([nota] * contagem[nota])

    return saida

input = sys.stdin.read
dados = input().split()

A = int(dados[0])

N = [int(dados[i]) for i in range(1, A + 1)]

vetor_ordenado = counting_sort_notas(N)

sys.stdout.write("\n".join(map(str, vetor_ordenado)) + "\n")
