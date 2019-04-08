#include <time.h> 
#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int vetor[], int tam_vetor) {
    /*
    Realiza ordenacao utilizando bubble sort
    vetor: Vetor de inteiros
    tam_vetor: Inteiro com tamanho do vetor
    */
    int escolhido, i, j;
    for (i = 1; i < tam_vetor; i++) {
        escolhido = vetor[i];
        j = i - 1;
        
        while ((j >= 0) && (vetor[j] > escolhido)) {
            vetor[j + 1] = vetor[j];
            j--;
        }
        
        vetor[j + 1] = escolhido;
    }
}