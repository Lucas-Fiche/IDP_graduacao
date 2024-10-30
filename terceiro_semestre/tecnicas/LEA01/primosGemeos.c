#include <stdio.h>
#include <math.h>

int verificaNumPrimo(int numero) {
    if (numero <= 1) {
        return 0; 
    }
    for (int j = 2; j <= sqrt(numero); j++) {
        if (numero % j == 0) {
            return 0; 
        }
    }
    return 1; 
}

int main() {
    int verificacao, numero;

    scanf("%d", &verificacao);

    for (int i = 0; i < verificacao; i++) {
        scanf("%d", &numero);

        if (verificaNumPrimo(numero) && (verificaNumPrimo(numero - 2) || verificaNumPrimo(numero + 2))) {
            printf("O numero %d eh um primo gemeo\n", numero);
        } else {
            printf("O numero %d nao eh um primo gemeo\n", numero);
        }
    }

    return 0;
}
