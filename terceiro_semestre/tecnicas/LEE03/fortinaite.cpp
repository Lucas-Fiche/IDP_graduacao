#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Jogador {
    string nome;
    int tempo;
    string tempoOriginal;

    int converteTempo(string t) {
        int minutos = stoi(t.substr(0, t.find(':')));
        int segundos = stoi(t.substr(t.find(':') + 1));
        return minutos * 60 + segundos;
    }

    Jogador(string n, string t) {
        nome = n;
        tempoOriginal = t;
        tempo = converteTempo(t);
    }
};

bool comparaJogadores(const Jogador &a, const Jogador &b) {
    if (a.tempo != b.tempo) {
        return a.tempo > b.tempo; 
    }
    return a.nome > b.nome; 
}

int main() {
    int J;
    cin >> J; 
    
    vector<Jogador> jogadores;
    
    for (int i = 0; i < J; i++) {
        string nome, tempo;
        cin >> nome >> tempo;
        jogadores.emplace_back(nome, tempo);
    }
    
    sort(jogadores.begin(), jogadores.end(), comparaJogadores);
    
    for (int i = 0; i < J; i++) {
        cout << (i + 1) << ". " << jogadores[i].tempoOriginal << " - " << jogadores[i].nome << endl;
    }

    return 0;
}
