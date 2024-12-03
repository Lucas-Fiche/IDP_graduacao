#include <iostream>
#include <iomanip>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casosTeste;
    cin >> casosTeste;

    for (int t = 0; t < casosTeste; ++t) {
        int produtosDisponiveis;
        cin >> produtosDisponiveis;

        unordered_map<string, double> tabelaPrecos;

        for (int i = 0; i < produtosDisponiveis; ++i) {
            string produto;
            double preco;
            cin >> produto >> preco;
            tabelaPrecos[produto] = preco;
        }

        int produtosComprados;
        cin >> produtosComprados;

        double totalGasto = 0.0;

        for (int i = 0; i < produtosComprados; ++i) {
            string produtoDesejado;
            int quantidade;
            cin >> produtoDesejado >> quantidade;

            if (tabelaPrecos.find(produtoDesejado) != tabelaPrecos.end()) {
                totalGasto += tabelaPrecos[produtoDesejado] * quantidade;
            }
        }

        cout << fixed << setprecision(2) << "R$ " << totalGasto << "\n";
    }

    return 0;
}
