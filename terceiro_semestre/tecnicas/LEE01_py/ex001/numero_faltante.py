N = int(input())
numeros = list(map(int, input().split()))
temp = 0

soma = (N *(N + 1))/2

for i in numeros:
    temp += i

numero_faltante = soma - temp
print(int(numero_faltante))