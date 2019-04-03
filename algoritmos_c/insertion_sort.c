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
        insertion_sort(vetor, j);
        t = clock() - t; 
        double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        printf("insertion sort com %d elementos demorou %f segundos \n", j, time_taken); 
    }
    return 0; 
}