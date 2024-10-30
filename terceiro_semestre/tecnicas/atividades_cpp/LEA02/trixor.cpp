#include <iostream>

using namespace std;

int main() {
    int T;  
    cin >> T;  

    while (T--) {
        long long int A, B, Y, C;
        cin >> A >> B >> Y;  

        C = A ^ B ^ Y;

        if (C >= 0 && C <= 10000000) {
            cout << C << endl;
        } else {
            cout << -1 << endl;
        }
    }

    return 0;
}

