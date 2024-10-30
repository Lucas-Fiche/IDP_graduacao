#include <stdio.h>

int main(void) {
  char nome_ra[] = {'L', 'u', 'c', 'a', 's', ' ', 'B', 'o', 'r', 'g', 'e', 's', ' ', '-', ' ', '2', '0', '2', '1', '0', '6', '8'};
  
//  int tamanho = (sizeof(nome) / sizeof(nome[0]))+(sizeof(ra)/sizeof(ra[0]));
    
  for(int i = 0; i < sizeof(nome_ra); i++){
    printf("%c", nome_ra[i]);
  }

  return 0;
}