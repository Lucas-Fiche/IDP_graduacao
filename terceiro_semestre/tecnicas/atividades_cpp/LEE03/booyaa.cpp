#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

long long calcular_media_aritmetica(const vector<int>& subscricoes) {
    long double soma = 0;
    for (int s : subscricoes) {
        soma += s;
    }
    return ceil(soma / 30.0);
}

void atualizar_subscricoes(vector<int>& subscricoes, long long nova_subscricao) {
    subscricoes.erase(subscricoes.begin());
    subscricoes.push_back(nova_subscricao);
}

long long calcular_total_seguidores(long long F, long long D, vector<int> subscricoes) {
    long long totalSeguidores = F;
    for (int dia = 0; dia < D; ++dia) {
        long long mediaAritmetica = calcular_media_aritmetica(subscricoes);
        totalSeguidores += mediaAritmetica;
        atualizar_subscricoes(subscricoes, mediaAritmetica);
    }
    return totalSeguidores;
}

int main() {
    long long F, D;
    cin >> F >> D;

    vector<int> subscricoes(30);
    for (int &s : subscricoes) {
        cin >> s;
    }

    long long totalSeguidores = calcular_total_seguidores(F, D, subscricoes);

    cout << totalSeguidores << endl;

    return 0;
}
