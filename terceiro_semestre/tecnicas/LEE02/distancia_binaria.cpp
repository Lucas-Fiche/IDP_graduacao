#include <iostream>
using namespace std;

int calcularHamming(int num1, int num2) {
    int xorComparar = num1 ^ num2;
    int distancia = 0;

    while (xorComparar > 0) {
        distancia += xorComparar & 1;
        xorComparar >>= 1;
    }
    
    return distancia;
}

int main() {
    int testes;
    cin >> testes;

    while (testes--) {
        int num1, num2;
        cin >> num1 >> num2;

        int distancia = calcularHamming(num1, num2);
        cout << distancia << endl;
    }

    return 0;
}
