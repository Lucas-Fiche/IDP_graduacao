#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int D;

    while (scanf("%d", &D) && D != -1) {
        char *num = malloc((D + 1) * sizeof(char));
        if (num == NULL) {
            return 1;
        }

        scanf("%s", num);

        int soma = 0;
        for (int i = 0; i < D; i++) {
            soma += num[i] - '0';
        }

        if (soma % 3 == 0) {
            printf("%d sim\n", soma);
        } else {
            printf("%d nao\n", soma);
        }

        free(num);
    }

    return 0;
}
