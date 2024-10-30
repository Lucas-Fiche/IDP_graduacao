#include <bits/stdc++.h>
using namespace std;

int contarPedras(const string &bloco) {
    int count = 0;
    int balance = 0;  

    for (char c : bloco) {
        if (c == '<') {
            balance++;  
        } else if (c == '>' && balance > 0) {
            count++;  
            balance--;  
        }
    }

    return count;  
}

int main() {
    int N;
    cin >> N;

    while (N--) {
        string bloco;
        cin >> bloco;
        cout << contarPedras(bloco) << endl;  
    }

    return 0;
}
