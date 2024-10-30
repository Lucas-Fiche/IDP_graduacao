def counting_sort(arr):
    # Identificar o valor máximo no array
    max_val = max(arr)

    # Criar o vetor de contagem (Uma lista de valor 0, com tamanho igual ao valor máximo + 1)
    # O incremento (+1) ocorre para ajustar o índice da lista. Se o valor máximo é 3, a lista precisa armazenar 4 espaços contando o 0.
    count = [0] * (max_val + 1)

    # Contar as ocorrências de cada número no array original
    # Para cada elemento i no arr passado como parâmetro da função, a lista count, no índice equivalente ao elemento, recebe count[i] + 1.
    for i in arr:
        count[i] += 1
    
    print("Lista Contagem: ", count)
    print("Índice:           0  1  2  3")

    # Cria uma lista vazia chamada output. Depois percorre todos os índices do vetor count (range(len(count)))
    output = []
    tamanho_count = range(len(count)) # len conta a quantidade de elementos na lista, e range monta a distância que o loop deve percorrer
    print("Tamanho do Vetor Count: ", tamanho_count)
    for i in range(len(count)):
        output.extend([i] * count[i]) # Adicionar o número 'i' 'count[i]' vezes
    
    return output

 # Testar couting sort
arr = [1, 0, 3, 1, 3, 1]
ordenado = counting_sort(arr)
print("Vetor Ordenado: ", ordenado)
   
