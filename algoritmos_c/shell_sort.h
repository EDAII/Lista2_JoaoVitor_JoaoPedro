#include <time.h> 
#include <stdio.h>
#include <stdlib.h>


void shell_sort(int vet[], int tam_vetor) {
    /*
    Realiza ordenacao utilizando bubble sort
    vetor: Vetor de inteiros
    tam_vetor: Inteiro com tamanho do vetor
    */
    int i , j , value;
    int gap = 1;
    while(gap < tam_vetor) {
        gap = 3 * gap + 1;
    }
    while ( gap > 1) {
        gap /= 3;
        for(i = gap; i < tam_vetor; i++) {
            value = vet[i];
            j = i;
            while (j >= gap && value < vet[j - gap]) {
                vet[j] = vet [j - gap];
                j = j - gap;
            }
            vet [j] = value;
        }
    }
}
