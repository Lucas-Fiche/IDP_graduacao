#include <bits/stdc++.h>
using namespace std;

int contarParafusosDoTipo(int tipoParafuso, const vector<pair<int, int>>& listaCaixas) {
    int contador = 0;
    for (const auto& caixa : listaCaixas) {
        if (caixa.first <= tipoParafuso && tipoParafuso <= caixa.second) {
            contador++;
        }
    }
    return contador;
}

void imprimirResultado(int tipoParafuso, int quantidade) {
    if (quantidade > 0) {
        cout << "Contem " << quantidade << " parafuso(s) do tipo " << tipoParafuso << endl;
    } else {
        cout << "Nao contem parafusos do tipo " << tipoParafuso << endl;
    }
}

int main() {
    int quantidadeCaixas, quantidadeConsultas;
    cin >> quantidadeCaixas >> quantidadeConsultas;

    vector<pair<int, int>> intervaloCaixas(quantidadeCaixas);  

    for (int i = 0; i < quantidadeCaixas; i++) {
        int menorTamanho, maiorTamanho;
        cin >> menorTamanho >> maiorTamanho;
        intervaloCaixas[i] = {menorTamanho, maiorTamanho};
    }

    while (quantidadeConsultas--) {
        int tipoParafusoConsultado;
        cin >> tipoParafusoConsultado;
        int quantidadeParafusos = contarParafusosDoTipo(tipoParafusoConsultado, intervaloCaixas);
        imprimirResultado(tipoParafusoConsultado, quantidadeParafusos);
    }

    return 0;
}
