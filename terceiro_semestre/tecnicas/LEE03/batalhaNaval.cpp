#include <bits/stdc++.h>
using namespace std;

void lerEntrada(int &N, int &M, int &Q, vector<int> &elementos) {
    scanf("%d %d %d", &N, &M, &Q);
    elementos.resize(N * M);
    for (int i = 0; i < N * M; i++) {
        scanf("%d", &elementos[i]);
    }
}

void processarConsultas(int M, int Q, vector<int> &elementos) {
    while (Q--) {
        int V;
        scanf("%d", &V);
        auto it = lower_bound(elementos.begin(), elementos.end(), V);

        if (it != elementos.end() && *it == V) {
            int index = distance(elementos.begin(), it);
            int row = index / M;
            int col = index % M;
            printf("%d %d\n", row, col);
        } else {
            printf("-1 -1\n");
        }
    }
}

int main() {
    int N, M, Q;
    vector<int> elementos;

    lerEntrada(N, M, Q, elementos);
    processarConsultas(M, Q, elementos);

    return 0;
}
