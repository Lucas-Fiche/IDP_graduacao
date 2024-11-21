def calcular_tamanho_maior_grupo(num_alunos, relacoes):
    grafo = {i: [] for i in range(1, num_alunos + 1)}
    
    for aluno_a, aluno_b in relacoes:
        grafo[aluno_a].append(aluno_b)
        grafo[aluno_b].append(aluno_a)

    visitados = set()
    maior_tamanho = 0

    def explorar_grupo(inicio):
        grupo = [inicio]
        tamanho = 0
        while grupo:
            aluno = grupo.pop()
            if aluno not in visitados:
                visitados.add(aluno)
                tamanho += 1
                grupo.extend(grafo[aluno])
        return tamanho

    for aluno in grafo:
        if aluno not in visitados:
            tamanho_atual = explorar_grupo(aluno)
            maior_tamanho = max(maior_tamanho, tamanho_atual)

    return maior_tamanho

def main():
    entrada = input().split()
    num_alunos, num_relacoes = int(entrada[0]), int(entrada[1])
    relacoes = [tuple(map(int, input().split())) for _ in range(num_relacoes)]
    
    maior_grupo = calcular_tamanho_maior_grupo(num_alunos, relacoes)
    print(f"O grupo mais numeroso tem {maior_grupo} aluno(s)")

if __name__ == "__main__":
    main()
