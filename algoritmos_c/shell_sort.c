#include <time.h> 
#include <stdio.h>
#include <stdlib.h>


void shell_sort(int vet[], int size) {
    int i , j , value;
    int gap = 1;
    while(gap < size) {
        gap = 3*gap+1;
    }
    while ( gap > 1) {
        gap /= 3;
        for(i = gap; i < size; i++) {
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

int main(){    
    int i, j;
    for(j = 100; j <= 1000; j+=100){
        srand(time(NULL));
        int vetor[j];
        int size = sizeof(vetor) / sizeof(vetor[0]); // pegando tamanho do array
        for(i = 0; i < size; i++){
            vetor[i] = rand() % j + 1; // gera nums aleatórios de 1 a 100
        }
        clock_t t;
        t = clock(); 
        shell_sort(vetor, j);
        t = clock() - t; 
        double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        printf("shell sort com %d elementos demorou %f segundos \n", j, time_taken); 
    }
    return 0; 
}