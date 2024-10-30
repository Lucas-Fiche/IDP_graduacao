def encontrar_pai(indice):
    return indice // 2

def main():
    total_nos, total_consultas = map(int, input().split())
    estrutura_arvore = [None] + list(map(int, input().split()))
    
    for _ in range(total_consultas):
        no_consulta = int(input().strip())
        
        if estrutura_arvore[1] == -1:
            print("NULL")
            break
        
        if no_consulta == 1:
            print("RAIZ")
            continue
        
        indice_pai = encontrar_pai(no_consulta)
        
        if indice_pai >= 1 and estrutura_arvore[indice_pai] != -1:
            print(estrutura_arvore[indice_pai])
        else:
            print("NULL")

if __name__ == "__main__":
    main()
