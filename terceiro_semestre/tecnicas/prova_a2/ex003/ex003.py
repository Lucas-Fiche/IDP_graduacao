def heterograma(palavra):
    return len(set(palavra)) == len(palavra)

quantidade = int(input())
palavras = [input().strip() for i in range(quantidade)]

for palavra in palavras:
    print("STRONGRAMA" if heterograma(palavra) else "WEAKORD")
