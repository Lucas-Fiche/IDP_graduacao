import sys
from collections import deque
import heapq

def main():
    entrada = sys.stdin.read().strip().split("\n")
    index = 0
    
    while index < len(entrada):
        n = int(entrada[index])
        index += 1

        pilha = []
        fila = deque()
        fila_prioridade = []
        
        eh_pilha = True
        eh_fila = True
        eh_fila_prioridade = True

        for _ in range(n):
            comando = list(map(int, entrada[index].split()))
            index += 1

            if comando[0] == 1:
                x = comando[1]
                if eh_pilha:
                    pilha.append(x)
                if eh_fila:
                    fila.append(x)
                if eh_fila_prioridade:
                    heapq.heappush(fila_prioridade, -x)
            elif comando[0] == 2:
                x = comando[1]
                if eh_pilha:
                    if not pilha or pilha.pop() != x:
                        eh_pilha = False
                if eh_fila:
                    if not fila or fila.popleft() != x:
                        eh_fila = False
                if eh_fila_prioridade:
                    if not fila_prioridade or -heapq.heappop(fila_prioridade) != x:
                        eh_fila_prioridade = False

        if eh_pilha and not eh_fila and not eh_fila_prioridade:
            print("stack")
        elif not eh_pilha and eh_fila and not eh_fila_prioridade:
            print("queue")
        elif not eh_pilha and not eh_fila and eh_fila_prioridade:
            print("priority queue")
        elif not eh_pilha and not eh_fila and not eh_fila_prioridade:
            print("impossible")
        else:
            print("not sure")

if __name__ == "__main__":
    main()
