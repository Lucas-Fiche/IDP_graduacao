#include <stdio.h>

int main(void) {
  int n1, n2;
  
  printf("Digite dois números: \n");
  scanf("%i %i", &n1, &n2);

  int soma = n1 + n2;
  int subtracao = n1 - n2;
  int multiplicacao = n1 * n2;
  float divisao = n1 / n2;
  float resto_divisao = n1 % n2;

  printf("A soma entre %i e %i é: %i\n", n1, n2, soma);
  printf("A subtração entre %i e %i é: %i\n", n1, n2, subtracao);
  printf("A multiplicação entre %i e %i é: %i\n", n1, n2, multiplicacao);
  printf("A divisão entre %i e %i é: %.1f\n", n1, n2, divisao);
  printf("O resto da divisão entre %i e %i é: %.1f\n", n1, n2, resto_divisao);
  return 0;
}