def lsb (numero):
    if numero == 0:
        return "None"
    else:
        posicao = 1
        while numero > 0:
            if numero & 1:
                return posicao
            numero >>= 1
            posicao += 1

N = int(input())

for i in range (N):
    numero = int(input())
    print(lsb(numero))