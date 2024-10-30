class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.esquerda is None:
                nodo.esquerda = Nodo(valor)
            else:
                self._inserir_recursivo(nodo.esquerda, valor)
        else:
            if nodo.direita is None:
                nodo.direita = Nodo(valor)
            else:
                self._inserir_recursivo(nodo.direita, valor)

    def percurso_em_ordem(self):
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _em_ordem_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._em_ordem_recursivo(nodo.esquerda, resultado)
            resultado.append(nodo.valor)
            self._em_ordem_recursivo(nodo.direita, resultado)

    def percurso_pre_ordem(self):
        resultado = []
        self._pre_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _pre_ordem_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.valor)
            self._pre_ordem_recursivo(nodo.esquerda, resultado)
            self._pre_ordem_recursivo(nodo.direita, resultado)

    def percurso_pos_ordem(self):
        resultado = []
        self._pos_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _pos_ordem_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._pos_ordem_recursivo(nodo.esquerda, resultado)
            self._pos_ordem_recursivo(nodo.direita, resultado)
            resultado.append(nodo.valor)

def main():
    quantidade_nodos = int(input())
    valores = list(map(int, input().split()))

    arvore = ArvoreBinariaBusca()
    for valor in valores:
        arvore.inserir(valor)

    print("In.:", " ".join(map(str, arvore.percurso_em_ordem())))
    print("Pre:", " ".join(map(str, arvore.percurso_pre_ordem())))
    print("Pos:", " ".join(map(str, arvore.percurso_pos_ordem())))

if __name__ == "__main__":
    main()
