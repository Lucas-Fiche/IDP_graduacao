#include <stdio.h>

int main() {
    unsigned long long int n, q, c, tmp;

    scanf("%llu %llu", &n, &q);

    for (int i = 0; i < q; i++){
        scanf("%llu", &c);

        tmp = (n >> c);
        if (tmp & 1) {
            puts("aceso");
        } else {
            puts("apagado");
        }
    }
    return 0;
}
