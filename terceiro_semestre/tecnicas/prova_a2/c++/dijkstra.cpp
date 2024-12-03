#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
    unordered_set<string> tiposJoias;
    string joia;

    while (cin >> joia) {
        if (tiposJoias.find(joia) == tiposJoias.end()) {
            tiposJoias.insert(joia);
        }
    }

    int quantidadeDistintas = tiposJoias.size();
    cout << quantidadeDistintas << "\n";

    return 0;
}
