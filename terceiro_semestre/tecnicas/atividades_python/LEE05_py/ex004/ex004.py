from collections import defaultdict

def encontrar_tripla(qtd, alvo, valores):
    numeros = defaultdict(list)
    for i, num in enumerate(valores):
        numeros[num].append(i)
    
    for i in range(qtd):
        for j in range(i + 1, qtd):
            terceiro = alvo - valores[i] - valores[j]
            
            if terceiro in numeros:
                for k in numeros[terceiro]:
                    if k > j:
                        return f"{valores[i]} {valores[j]} {valores[k]}"
    
    return "Nao existe"

def main():
    qtd, alvo = map(int, input().split())
    
    valores = list(map(int, input().split()))
    
    print(encontrar_tripla(qtd, alvo, valores))

if __name__ == "__main__":
    main()