import sys
from collections import defaultdict

def principal():
    medalhas = defaultdict(lambda: [0, 0, 0])

    try:
        while True:
            prova = input().strip()
            ouro = input().strip()
            prata = input().strip()
            bronze = input().strip()

            medalhas[ouro][0] += 1
            medalhas[prata][1] += 1
            medalhas[bronze][2] += 1
    except EOFError:
        pass

    medalhas_ordenadas = sorted(medalhas.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))

    print("Quadro de Medalhas")
    for pais, (ouro, prata, bronze) in medalhas_ordenadas:
        print(f"{pais} {ouro} {prata} {bronze}")

if __name__ == "__main__":
    principal()
