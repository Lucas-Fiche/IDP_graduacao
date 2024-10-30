#include <stdio.h>
#include <math.h>

int main(void) {
  float n1, n2, n3;
  double n4;
  
  printf("Digite um número negativo: \n");
  scanf("%lf", &n4);
  

  //Valor Absoluto (Módulo)
  printf("Valor Absoluto de %.1f é %.1f\n", n4, fabs(n4));

  printf("Digite dois números: \n");
  scanf("%f %f", &n1, &n2);
  
  //Potência
  printf("Potência de %.1f^%.1f = %.2f\n", n1, n2, pow(n1, n2));

  //Raiz Quadrada
  printf("Raiz Quadrada de %.1f = %.2f\n", n1, sqrt(n1));

  printf("Digite um número decimal: \n");
  scanf("%f", &n3);
  
  //Menor nº Inteiro (Aproximação)
  printf("O menor nº inteiro mais próximo de %.2f é %.1f\n", n3, floor(n3));

  //Maior nº Inteiro (Aproximação)
  printf("O maior nº inteiro mais próximo de %.2f é %.1f\n", n3, ceil(n3));

  //nº de Euler elevado a n1
  printf("Número de Euler (2.71) elevado a %.1f = %.2f", n1, exp(n1));
    
  return 0;
}