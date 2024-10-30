D = int(input())

while D != -1:
    N = input()
    soma_digitos = 0

    for digito in N:
        soma_digitos += int(digito)

    if soma_digitos % 3 == 0:
        print(f'{soma_digitos} sim')
    else:
        print(f'{soma_digitos} nao')

    D = int(input())
