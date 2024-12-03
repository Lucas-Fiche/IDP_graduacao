from collections import defaultdict

def corredor_dos_assassinos():
    import sys
    entrada = sys.stdin.read
    dados = entrada().splitlines()

    assassinos = defaultdict(int)
    assassinados = set()

    for linha in dados:
        assassino, assassinado = linha.split()
        assassinos[assassino] += 1
        assassinados.add(assassinado)

    nomes_assassinos = [nome for nome in assassinos if nome not in assassinados]
    nomes_assassinos.sort()

    print("HALL OF MURDERERS")
    for nome in nomes_assassinos:
        print(nome, assassinos[nome])

if __name__ == "__main__":
    corredor_dos_assassinos()
