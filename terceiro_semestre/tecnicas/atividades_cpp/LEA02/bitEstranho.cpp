#include <iostream>
using namespace std;

int main() {
    int N, B;
    cin >> N >> B;

    for (int i = 0; i < N; i++) {
        int V;
        cin >> V;
        V = V & ~(1 << B);
        cout << V << endl;
    }

    return 0;
}
