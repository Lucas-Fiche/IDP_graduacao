#include <stdio.h>

int main() {
    long long int num;
    scanf("%lld", &num);

    long long int soma_esperada = (num * (num + 1)) / 2;

    long long int soma_fornecida = 0;
    long long int temp;

    for (int i = 0; i < num - 1; i++) {
        scanf("%lld", &temp);
        soma_fornecida += temp;
    }

    long long int num_faltante = soma_esperada - soma_fornecida;
    printf("%lld\n", num_faltante);

    return 0;
}