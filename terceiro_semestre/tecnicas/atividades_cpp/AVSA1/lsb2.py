def lsb(numero):
    if numero == 0:
        return "None"
    else:
        numero_binario = bin(numero)[2:]
        inverter_binario = numero_binario[::-1]
        return inverter_binario.index('1') + 1

N = int(input())

for i in range(N):
    numero = int(input())
    print(lsb(numero))

# 285097195