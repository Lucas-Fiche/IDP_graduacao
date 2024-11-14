def main():
    T = int(input().strip())
    
    for _ in range(T):
        linha = input().strip()
        catalogo, pedras = linha.split()
        
        disponivel = set(catalogo)
        
        negociaveis = sum(1 for p in pedras if p in disponivel)
        
        print(f"Contem {negociaveis} pedras negociaveis")

if __name__ == "__main__":
    main()
