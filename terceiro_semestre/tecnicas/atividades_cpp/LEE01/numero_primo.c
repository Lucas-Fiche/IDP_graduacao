#include <stdio.h>
#include <math.h> 

int main() {
    int verificacao, numero;


    scanf("%d", &verificacao);

    for (int i = 0; i < verificacao; i++) {
        int contador = 1; 
        scanf("%d", &numero);

        if (numero <= 1) {
            contador = 0; 
        } else {
            
            for (int j = 2; j <= sqrt(numero); j++) {
                if (numero % j == 0) {
                    contador = 0; 
                    break;
                }
            }
        }

        if (contador) {
            printf("o numero %d eh primo\n", numero);
        } else {
            printf("o numero %d nao eh primo\n", numero);
        }
    }

    return 0;
}


