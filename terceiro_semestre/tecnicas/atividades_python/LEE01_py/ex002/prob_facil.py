N = int(input())
sequencia = list()

while N != 1:

    sequencia.append(N)

    if N % 2 == 0:
        N = N//2
    elif N % 2 != 0:
        N = 3*N + 1

sequencia.append(1)

print(' '.join(map(str, sequencia)))