#include <iostream>
#include <deque>
using namespace std;


deque<int> inicializarBaralho(int numeroCartas) {
    deque<int> cartas;
    for (int i = numeroCartas; i >= 1; i--) {
        cartas.push_back(i);  
    }
    return cartas;
}

void processarDescarte(deque<int>& cartas) {
    bool primeiroDescarte = true;
    cout << "Descarte: ";
    while (cartas.size() > 1) {
        if (!primeiroDescarte) {
            cout << ", ";
        }
        cout << cartas.front(); 
        cartas.pop_front(); 

        int cartaMover = cartas.front();
        cartas.pop_front(); 
        cartas.push_back(cartaMover);  
        primeiroDescarte = false;
    }
    cout << endl;
}

void mostrarUltimaCarta(const deque<int>& cartas) {
    cout << "Ultima carta: " << cartas.front() << endl;  
}

int main() {
    int numeroCartas;
    cin >> numeroCartas;

    deque<int> cartas = inicializarBaralho(numeroCartas);  
    processarDescarte(cartas);  
    mostrarUltimaCarta(cartas);  

    return 0;
}

