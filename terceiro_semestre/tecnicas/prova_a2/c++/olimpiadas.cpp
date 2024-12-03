#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Medalhas {
    int ouro = 0;
    int prata = 0;
    int bronze = 0;
};

int main() {
    unordered_map<string, Medalhas> quadro;
    string modalidade, ouro, prata, bronze;

    while (getline(cin, modalidade)) {
        getline(cin, ouro);
        getline(cin, prata);
        getline(cin, bronze);

        quadro[ouro].ouro++;
        quadro[prata].prata++;
        quadro[bronze].bronze++;
    }

    vector<pair<string, Medalhas>> paises(quadro.begin(), quadro.end());

    sort(paises.begin(), paises.end(), [](const pair<string, Medalhas>& a, const pair<string, Medalhas>& b) {
        if (a.second.ouro != b.second.ouro) {
            return a.second.ouro > b.second.ouro;
        }
        if (a.second.prata != b.second.prata) {
            return a.second.prata > b.second.prata;
        }
        if (a.second.bronze != b.second.bronze) {
            return a.second.bronze > b.second.bronze;
        }
        return a.first < b.first;
    });

    cout << "Quadro de Medalhas" << "\n";
    for (const auto& pais : paises) {
        cout << pais.first << " " << pais.second.ouro << " " << pais.second.prata << " " << pais.second.bronze << "\n";
    }

    return 0;
}
