index = 0
dados = []

while True:
    D = int(input())
    if D == -1:
        break
    N = input()
    dados.append((D, N))

for D, N in dados:
    soma_impares = 0
    soma_pares = 0

    for i in range(len(N)):
        digito = int(N[i])
        if i % 2 == 0:
            soma_impares += digito
        else:
            soma_pares += digito

    diferenca = soma_impares - soma_pares
    divisivel = diferenca % 11 == 0
    resultado = "sim" if divisivel else "não"

    print(f"{N}: {soma_impares} - {soma_pares} = {diferenca} - {resultado}")
