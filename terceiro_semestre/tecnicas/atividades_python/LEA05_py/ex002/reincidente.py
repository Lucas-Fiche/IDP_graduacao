def main():
    lista = {}
    
    while True:
        entrada = input().strip()
        
        if entrada == "fim 0":
            break

        S, A = entrada.split()
        A = int(A)
        
        if S in lista:
            print(f"{S} eh reincidente com {lista[S]} crime(s)")
            lista[S] += 1
        else:
            lista[S] = 1
            print(f"{S} eh reu primario")

if __name__ == "__main__":
    main()
