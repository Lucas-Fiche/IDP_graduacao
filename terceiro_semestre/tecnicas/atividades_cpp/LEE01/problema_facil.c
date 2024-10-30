#include <stdio.h>

int main(){
    long long int numero_inteiro;

    scanf("%lld", &numero_inteiro);

    while (numero_inteiro != 1){
        printf("%lld ", numero_inteiro);
        if (numero_inteiro % 2 == 0){
            numero_inteiro /= 2;
        } else {
            numero_inteiro = numero_inteiro * 3 + 1;
        }
    }

    printf("%lld\n", numero_inteiro);

    return 0;
}