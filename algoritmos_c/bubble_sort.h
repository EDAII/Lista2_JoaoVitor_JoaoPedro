#include <time.h> 
#include <stdio.h>
#include <stdlib.h>

void bubble_sort (int vetor[], int tam_vetor) {
    /*
    Realiza ordenacao utilizando bubble sort
    vetor: Vetor de inteiros
    tam_vetor: Inteiro com tamanho do vetor
    */
    int i, j, aux;

    for (i = 1; i < tam_vetor; i++) {
        for (j = 0; j < tam_vetor - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
}