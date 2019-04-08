#include <time.h> 
#include <stdio.h>
#include <stdlib.h>

void selection_sort(int vetor[], int tam_vetor) {
  /*
    Realiza ordenacao utilizando bubble sort
    vetor: Vetor de inteiros
    tam_vetor: Inteiro com tamanho do vetor
  */
  int i, j, min, aux;
  for (i = 0; i < (tam_vetor-1); i++) 
  {
     min = i;
     for (j = (i+1); j < tam_vetor; j++) {
       if(vetor[j] < vetor[min]) 
         min = j;
     }
     if (vetor[i] != vetor[min]) {
       aux = vetor[i];
       vetor[i] = vetor[min];
       vetor[min] = aux;
     }
  }
}