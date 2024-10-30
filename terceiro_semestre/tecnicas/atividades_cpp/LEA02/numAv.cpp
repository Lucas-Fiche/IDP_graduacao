#include <iostream>

using namespace std;

int main() {
    unsigned int n;
    cin >> n; 

    unsigned int resultado = 0;

    for (int i = 0; i < 32; i++) {
        resultado = (resultado << 1) | (n & 1);  
        n >>= 1; 
    }

    cout << resultado << endl;  
    return 0;
}
