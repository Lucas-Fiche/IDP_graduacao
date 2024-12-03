#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    unordered_map<string, int> registroMortes;
    unordered_set<string> listaMortos;
    string autor, vitima;

    while (cin >> autor >> vitima) {
        if (registroMortes.find(autor) == registroMortes.end()) {
            registroMortes[autor] = 0;
        }
        registroMortes[autor]++;
        listaMortos.insert(vitima);
    }

    vector<string> nomesVivos;
    for (const auto& item : registroMortes) {
        if (listaMortos.find(item.first) == listaMortos.end()) {
            nomesVivos.push_back(item.first);
        }
    }

    sort(nomesVivos.begin(), nomesVivos.end());

    cout << "HALL OF MURDERERS" << "\n";
    for (const string& nome : nomesVivos) {
        cout << nome << " " << registroMortes[nome] << "\n";
    }

    return 0;
}
