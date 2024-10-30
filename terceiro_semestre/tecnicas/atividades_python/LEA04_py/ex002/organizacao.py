def processar_participantes(P, S, formularios, feedbacks):
    resultados = []
    
    escolhas = {}
    for form in formularios:
        nome = form[0]
        brindes = form[1:]
        escolhas[nome] = brindes
    
    for feedback in feedbacks:
        nome = feedback[0]
        brinde_recebido = feedback[1]
        
        if nome not in escolhas:
            if brinde_recebido:
                resultados.append(f"{nome} queria ganhar qualquer coisa e ganhou {brinde_recebido}!")
            continue

        if brinde_recebido in escolhas[nome]:
            resultados.append(f"{nome} conseguiu ganhar {brinde_recebido}!")
        else:
            resultados.append(f"{nome} infelizmente ganhou {brinde_recebido}...")
            
    return resultados

def main():
    P, S = map(int, input().split())
    
    formularios = []
    for _ in range(P):
        linha = input().split()
        formularios.append(linha)
    
    feedbacks = []
    for _ in range(S):
        linha = input().split()
        feedbacks.append(linha)
    
    resultados = processar_participantes(P, S, formularios, feedbacks)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()