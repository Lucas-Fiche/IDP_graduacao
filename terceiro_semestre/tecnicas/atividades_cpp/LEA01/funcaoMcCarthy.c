#include <stdio.h>

int funcaoMcCarthy(int numero) {
    if (numero > 100) {
        return numero - 10;
    } else {
        return funcaoMcCarthy(funcaoMcCarthy(numero + 11));
    }
}

int main() {
    int numeroTestes;
    int numero1, numero2;

    scanf("%d", &numeroTestes);

    for (int i = 0; i < numeroTestes; i++) {
        scanf("%d", &numero1);

        int resultado1 = funcaoMcCarthy(numero1);

        printf("%d\n", resultado1);
    }

    return 0;
}
