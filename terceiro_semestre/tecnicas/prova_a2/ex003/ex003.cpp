#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

bool ehHeterograma(const string& palavra) {
    unordered_set<char> caracteres;
    for (char caractere : palavra) {
        if (!isalnum(caractere)) continue;
        char caractereMinusculo = tolower(caractere);
        if (caracteres.count(caractereMinusculo)) return false;
        caracteres.insert(caractereMinusculo);
    }
    return true;
}

int main() {
    int quantidade;
    cin >> quantidade;

    string palavra;
    for (int i = 0; i < quantidade; ++i) {
        cin >> palavra;
        if (ehHeterograma(palavra)) {
            cout << "STRONGRAMA" << endl;
        } else {
            cout << "WEAKORD" << endl;
        }
    }

    return 0;
}
