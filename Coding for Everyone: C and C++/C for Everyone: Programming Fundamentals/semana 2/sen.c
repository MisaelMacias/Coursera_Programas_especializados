#include <stdio.h>
#include <math.h>

int main()
{
  double seno, numero;
  printf(" Introduzca un numero para calcular su seno:  ");
  scanf("%lf", &numero);
  
  seno = sin(numero);
  
  printf("\n El seno de %lf  es %f ", numero, seno);
  
  return 0;
}