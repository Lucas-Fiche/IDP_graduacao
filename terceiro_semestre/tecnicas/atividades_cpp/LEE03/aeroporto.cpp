#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    queue<string> norte, sul, leste, oeste;
    string direcao, aviao;

    while (cin >> direcao && direcao != "0") {
        while (cin >> aviao && aviao[0] == 'B') {
            if (direcao == "N") {
                norte.push(aviao);
            } else if (direcao == "S") {
                sul.push(aviao);
            } else if (direcao == "L") {
                leste.push(aviao);
            } else if (direcao == "O") {
                oeste.push(aviao);
            }
        }
        cin.putback(aviao[0]);
    }

    bool primeiro = true;
    
    while (!norte.empty() || !sul.empty() || !leste.empty() || !oeste.empty()) {
        if (!norte.empty()) {
            if (!primeiro) cout << " ";
            cout << norte.front();
            norte.pop();
            primeiro = false;
        }
        if (!sul.empty()) {
            if (!primeiro) cout << " ";
            cout << sul.front();
            sul.pop();
            primeiro = false;
        }
        if (!leste.empty()) {
            if (!primeiro) cout << " ";
            cout << leste.front();
            leste.pop();
            primeiro = false;
        }
        if (!oeste.empty()) {
            if (!primeiro) cout << " ";
            cout << oeste.front();
            oeste.pop();
            primeiro = false;
        }
    }

    cout << endl;
    return 0;
}
