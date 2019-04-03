#include <time.h> 
#include <stdio.h>
#include <stdlib.h>

void bubble_sort (int vetor[], int n) {
    int k, j, aux;

    for (k = 1; k < n; k++) {
        for (j = 0; j < n - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
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
        bubble_sort(vetor, j);
        t = clock() - t; 
        double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        printf("bubble sort com %d elementos demorou %f segundos \n", j, time_taken); 
    }
    return 0; 
}