import sys
input = sys.stdin.read

def main():
    dados = input().split()
    total_alunos = int(dados[0])
    
    frequencia_notas = [0] * 11
    
    for i in range(1, total_alunos + 1):
        nota = int(dados[i])
        frequencia_notas[nota] += 1
    
    resultado = []
    for i in range(11):
        if frequencia_notas[i] > 0:
            resultado.append(f"{i}\n" * frequencia_notas[i])
    
    sys.stdout.write("".join(resultado))

if __name__ == "__main__":
    main()
