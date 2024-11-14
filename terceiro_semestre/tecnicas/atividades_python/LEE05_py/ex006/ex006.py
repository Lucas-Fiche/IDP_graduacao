import heapq

class Pokemon:
    def __init__(self, nome, forca, index):
        self.nome = nome
        self.forca = forca
        self.index = index

    def __lt__(self, other):
        if self.forca == other.forca:
            if self.nome == other.nome:
                return self.index < other.index
            return self.nome < other.nome
        return self.forca > other.forca  

def main():
    P = int(input().strip())
    pokemons = []

    for i in range(P):
        dados = input().strip().split()
        nome = dados[0]
        forca = int(dados[1])
        pokemons.append(Pokemon(nome, forca, i))

    arena = pokemons[:]
    heapq.heapify(arena)
    resultados = []

    while len(arena) > 1:
        p1 = heapq.heappop(arena)
        p2 = heapq.heappop(arena)

        if p1.forca == p2.forca:
            resultados.append(f"{p1.nome} ({p1.forca}) x ({p2.forca}) {p2.nome} : empate")
        else:
            if p1.forca > p2.forca:
                resultados.append(f"{p1.nome} ({p1.forca}) x ({p2.forca}) {p2.nome} : {p1.nome} venceu")
                p1.forca -= p2.forca
                heapq.heappush(arena, p1)
            else:
                resultados.append(f"{p2.nome} ({p2.forca}) x ({p1.forca}) {p1.nome} : {p2.nome} venceu")
                p2.forca -= p1.forca
                heapq.heappush(arena, p2)

    if arena:
        vencedor = heapq.heappop(arena)
        resultados.append(f"{vencedor.nome} venceu com {vencedor.forca}")
    else:
        resultados.append("nenhum vencedor")

    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
