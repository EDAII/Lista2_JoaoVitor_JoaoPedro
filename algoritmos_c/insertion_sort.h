#include <time.h> 
#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int vetor[], int tamanhoVetor) {
    int escolhido, j;
    for (int i = 1; i < tamanhoVetor; i++) {
        escolhido = vetor[i];
        j = i - 1;
        
        while ((j >= 0) && (vetor[j] > escolhido)) {
            vetor[j + 1] = vetor[j];
            j--;
        }
        
        vetor[j + 1] = escolhido;
    }
}