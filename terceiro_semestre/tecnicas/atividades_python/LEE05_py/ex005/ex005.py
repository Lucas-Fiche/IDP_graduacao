def verificar_anagramas(casos):
    resultados = []
    
    for palavra1, palavra2 in casos:
        if len(palavra1) != len(palavra2):
            resultados.append("DIFERENTES")
            continue
        
        contagem = [0] * 128
        
        for c1, c2 in zip(palavra1, palavra2):
            contagem[ord(c1)] += 1
            contagem[ord(c2)] -= 1
        
        if all(count == 0 for count in contagem):
            resultados.append("ANAGRAMAS")
        else:
            resultados.append("DIFERENTES")
    
    return resultados

if __name__ == "__main__":
    qtd = int(input().strip())
    casos = [input().strip().split() for _ in range(qtd)]
    resultados = verificar_anagramas(casos)
    
    for resultado in resultados:
        print(resultado)
