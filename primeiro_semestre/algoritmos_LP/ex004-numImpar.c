#include <stdio.h>

int main(void) {
  int numeros[10];
  int contador_impares = 0;
  
  printf("Digite 10 números inteiros positivos: \n");
  for (int i = 0; i < 10; i++){
    int n;
    scanf("%d", &n);
    numeros[i] = n;
    if (numeros[i]%2 != 0){
      contador_impares += 1;
    }
  }

  int contador = 1;
  for (int i = 0; i < 10; i++){
  printf("%iº Valor: %i\n", contador, numeros[i]);
    contador += 1;
  }

  printf("Foram digitados %i números ímpares.\n", contador_impares);
  return 0;
}