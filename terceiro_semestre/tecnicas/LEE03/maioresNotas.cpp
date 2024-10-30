#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int A, Q;
    cin >> A >> Q;

    vector<int> notas(A);
    for (int i = 0; i < A; i++) {
        cin >> notas[i];
    }

    for (int i = 0; i < Q; i++) {
        int Cj;
        cin >> Cj;

        auto it = upper_bound(notas.begin(), notas.end(), Cj);

        int notas_maiores = distance(it, notas.end());

        cout << notas_maiores << " notas maiores que " << Cj << endl;
    }

    return 0;
}
