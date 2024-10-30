def obter_pai(no, estrutura_arvore):
    if no == 1:
        return "RAIZ"
    pai_indice = no // 2
    return estrutura_arvore[pai_indice - 1] if estrutura_arvore[pai_indice - 1] != -1 else "NULL"

def obter_filho(no, lado, estrutura_arvore, total_nos):
    indice_filho = 2 * no if lado == "esquerdo" else 2 * no + 1
    if indice_filho <= total_nos and estrutura_arvore[indice_filho - 1] != -1:
        return estrutura_arvore[indice_filho - 1]
    return "NULL"

def processar_consulta(no, estrutura_arvore, total_nos):
    pai = obter_pai(no, estrutura_arvore)
    filho_esquerdo = obter_filho(no, "esquerdo", estrutura_arvore, total_nos)
    filho_direito = obter_filho(no, "direito", estrutura_arvore, total_nos)
    return f"{pai} - {filho_esquerdo} {filho_direito}"

def resolver_arvore(quantidade_nos, lista_arvore, consultas):
    if lista_arvore[0] == -1:  
        return ["NULL" for _ in consultas]
    
    resultados = []
    for no in consultas:
        resultado_consulta = processar_consulta(no, lista_arvore, quantidade_nos)
        resultados.append(resultado_consulta)
    return resultados

quantidade_nos, total_consultas = map(int, input().split())
lista_arvore = list(map(int, input().split()))
consultas = [int(input()) for _ in range(total_consultas)]

resultados_final = resolver_arvore(quantidade_nos, lista_arvore, consultas)
for linha in resultados_final:
    print(linha)
