def checar_arquivos(num_testes, lista_casos):
    resultados = []
    
    for idx in range(num_testes):
        num_linhas, dados_linhas = lista_casos[idx]
        registros_unicos = set()
        contador_erros = 0
        
        for matricula_aluno, nome_disciplina in dados_linhas:
            if (matricula_aluno, nome_disciplina) in registros_unicos:
                contador_erros += 1
            else:
                registros_unicos.add((matricula_aluno, nome_disciplina))
        
        if contador_erros == 0:
            resultados.append("Arquivo OK")
        else:
            resultados.append(f"Corrompido com {contador_erros} erro(s)")
    
    return resultados

num_testes = int(input())
lista_casos = []

for _ in range(num_testes):
    num_linhas = int(input())
    dados_linhas = []
    for _ in range(num_linhas):
        entrada = input().split()
        matricula_aluno = int(entrada[0])
        nome_disciplina = entrada[1]
        dados_linhas.append((matricula_aluno, nome_disciplina))
    lista_casos.append((num_linhas, dados_linhas))

resultados = checar_arquivos(num_testes, lista_casos)
for resultado in resultados:
    print(resultado)
