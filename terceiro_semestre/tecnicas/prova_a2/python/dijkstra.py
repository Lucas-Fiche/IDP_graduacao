def contar_joias_distintas():
    joias = set()
    
    while True:
        joia = input().strip()
        if not joia:
            break
        joias.add(joia)

    print(len(joias))

if __name__ == "__main__":
    contar_joias_distintas()
