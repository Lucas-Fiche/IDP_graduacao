#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isPossible(const vector<long long>& exercicios, long long maxExerciciosPorSessao, long long horasDisponiveis) {
    long long horasNecessarias = 0;
    
    for (long long e : exercicios) {
        horasNecessarias += (e + maxExerciciosPorSessao - 1) / maxExerciciosPorSessao;
        if (horasNecessarias > horasDisponiveis) {
            return false;
        }
    }
    
    return horasNecessarias <= horasDisponiveis;
}

int main() {
    long long N, H;
    cin >> N >> H;
    
    vector<long long> exercicios(N);
    long long maxExercicios = 0;
    
    for (long long i = 0; i < N; i++) {
        cin >> exercicios[i];
        maxExercicios = max(maxExercicios, exercicios[i]);
    }
    
    long long left = 1, right = maxExercicios, resposta = maxExercicios;
    
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        
        if (isPossible(exercicios, mid, H)) {
            resposta = mid;
            right = mid - 1; 
        } else {
            left = mid + 1;  
        }
    }
    
    cout << resposta << endl;
    
    return 0;
}
