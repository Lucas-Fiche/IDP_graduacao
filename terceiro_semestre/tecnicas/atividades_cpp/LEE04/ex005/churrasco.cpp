#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
    int A;
    cin >> A;

    // Conjunto para armazenar todos os itens únicos do churrasco
    set<string> itens_churrasco;

    // Processamento dos itens de cada aluno
    for (int i = 0; i < A; ++i) {
        int P;
        cin >> P;
        cin.ignore(); // Ignora o newline após o número de itens

        for (int j = 0; j < P; ++j) {
            string item;
            getline(cin, item);

            // Verificação e adição do item no conjunto
            if (itens_churrasco.find(item) != itens_churrasco.end()) {
                cout << item << " ja tem" << endl;
            } else {
                cout << "adicionando " << item << endl;
                itens_churrasco.insert(item);
            }
        }
    }

    // Impressão dos itens finais em ordem alfabética
    cout << "Itens do churrasco:" << endl;
    for (const auto& item : itens_churrasco) {
        cout << item << endl;
    }

    return 0;
}
