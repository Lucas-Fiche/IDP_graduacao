#include <stdio.h>

//Função para Criação da Matriz Nula
void matrizNula(int n, int matriz[n][n]){
  printf("Matriz Nula: \n");
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++) {
      matriz[i][j] = 0;
      printf("%d\t", matriz[i][j]);
    }
    printf("\n");
  }
}

//Função para Criação da Matriz Identidade Plus

//    0 1 2
// 0  1 0 0
// 1  0 1 0
// 2  0 0 1
void matrizIdentidade(int n, int matrizIdentidade[n][n]){
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      if (i == j || i + j == n - 1){
        matrizIdentidade[i][j] = 1;
      } else {
        matrizIdentidade[i][j] = 0;
      }
      printf("%d\t", matrizIdentidade[i][j]);
    }
    printf("\n");
  }
}

int main(void) {
  int n;
  int opcao_menu = 0;

//Menu para escolha de qual matriz deseja criar
  printf("Qual matriz você deseja visualizar: \n");
  printf("1 - Matriz Nula \n");
  printf("2 - Matriz Identidade Plus \n");
  scanf("%d", &opcao_menu);

//estrutura de decisão para definir o tamanho da matriz e chamar as funções
  if (opcao_menu == 1){
    printf("Qual será o tamanho da Matriz Nula?\n");
    scanf("%d", &n);
    int matriz[n][n];
    matrizNula(n, matriz);
  } else {
    printf("Qual será o tamanho da Matriz Identidade Plus? \n");
    scanf("%d", &n);
    int matriz[n][n];
    matrizIdentidade(n, matriz);
  }


  return 0;
}