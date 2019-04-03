#include <time.h> 
#include <stdio.h>
#include <stdlib.h>

void selection_sort(int num[], int tam) { 
  int i, j, min, aux;
  for (i = 0; i < (tam-1); i++) 
  {
     min = i;
     for (j = (i+1); j < tam; j++) {
       if(num[j] < num[min]) 
         min = j;
     }
     if (num[i] != num[min]) {
       aux = num[i];
       num[i] = num[min];
       num[min] = aux;
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
        selection_sort(vetor, j);
        t = clock() - t; 
        double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        printf("selection sort com %d elementos demorou %f segundos \n", j, time_taken); 
    }
    return 0; 
}