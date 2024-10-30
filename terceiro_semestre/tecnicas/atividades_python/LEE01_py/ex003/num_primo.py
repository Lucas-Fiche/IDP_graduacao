N = int(input())

while N != 0:

    numero = int(input())
    
    primo = True

    if numero <= 1:
        primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break
    
    if primo:
        print(f'o numero {numero} eh primo')
    else:
        print(f'o numero {numero} nao eh primo')

    N-=1

