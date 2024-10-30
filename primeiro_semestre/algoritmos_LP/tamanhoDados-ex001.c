#include <stdio.h>

int main(void) {
  char c;
  int i;
  short s;
  float f;
  double d;
  long l;

  printf("Tamanho de char: %d bytes.\n", sizeof(c));
  printf("Tamanho de int: %d bytes. \n", sizeof(i));
  printf("Tamanho de short: %d bytes. \n", sizeof(s));
  printf("Tamanho de float: %d bytes. \n", sizeof(f));
  printf("Tamanho de double: %d bytes \n", sizeof(d));
  printf("Tamanho de long: %d bytes. \n", sizeof(l));
  return 0;
}