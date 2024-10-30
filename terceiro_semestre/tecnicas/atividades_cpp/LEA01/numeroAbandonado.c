#include <stdio.h>

int main() {
    int numerosPresentes;

    while (1) {
        scanf("%d", &numerosPresentes);

        if (numerosPresentes == -1) {
            break;
        }

        if (numerosPresentes <= 0 || numerosPresentes % 2 == 0) {
            continue;
        }

        int numeroFesta, resultado = 0;
        for (int i = 0; i < numerosPresentes; i++) {
            scanf("%d", &numeroFesta);
            resultado ^= numeroFesta;  
        }

        printf("%d\n", resultado);
    }

    return 0;
}

