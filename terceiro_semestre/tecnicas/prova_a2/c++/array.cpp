#include <iostream>
#include <vector>
#include <string>

using namespace std;

int calculaSomaHash(const vector<string>& linhas) {
    int hashTotal = 0;
    for (size_t linhaIndex = 0; linhaIndex < linhas.size(); ++linhaIndex) {
        const string& linha = linhas[linhaIndex];
        for (size_t caractereIndex = 0; caractereIndex < linha.size(); ++caractereIndex) {
            int valorChar = linha[caractereIndex] - 'A';
            hashTotal += valorChar + linhaIndex + caractereIndex;
        }
    }
    return hashTotal;
}

int main() {
    int casos;
    cin >> casos;

    vector<int> resultados;
    for (int c = 0; c < casos; ++c) {
        int linhas;
        cin >> linhas;
        cin.ignore();

        vector<string> entrada(linhas);
        for (int l = 0; l < linhas; ++l) {
            getline(cin, entrada[l]);
        }

        int resultado = calculaSomaHash(entrada);
        resultados.push_back(resultado);
    }

    for (int resultado : resultados) {
        cout << resultado << endl;
    }

    return 0;
}
