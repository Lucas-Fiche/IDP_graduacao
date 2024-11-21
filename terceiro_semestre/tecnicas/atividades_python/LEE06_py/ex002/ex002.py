def verificar_grupos(total_alunos, total_amizades, conexoes):
    grafo = {aluno: [] for aluno in range(1, total_alunos + 1)}
    for u, v in conexoes:
        grafo[u].append(v)
        grafo[v].append(u)
    
    visitados = set()
    grupos = 0

    def explorar_componente(aluno):
        stack = [aluno]
        while stack:
            atual = stack.pop()
            if atual not in visitados:
                visitados.add(atual)
                stack.extend(grafo[atual])

    for aluno in range(1, total_alunos + 1):
        if aluno not in visitados:
            grupos += 1
            explorar_componente(aluno)

    return "Todo mundo eh amigo de todo mundo" if grupos == 1 else "Varios grupos de amigos"

def main():
    entrada = input().split()
    total_alunos = int(entrada[0])
    total_amizades = int(entrada[1])
    conexoes = [tuple(map(int, input().split())) for _ in range(total_amizades)]
    resultado = verificar_grupos(total_alunos, total_amizades, conexoes)
    print(resultado)

if __name__ == "__main__":
    main()
