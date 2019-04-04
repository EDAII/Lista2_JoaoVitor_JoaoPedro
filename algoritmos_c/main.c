#include <time.h> 
#include <stdio.h>
#include <stdlib.h>
#include "insertion_sort.h"
#include "shell_sort.h"
#include "bubble_sort.h"
#include "selection_sort.h"


int main(){
    FILE *fp;    
    fp = fopen ("../csv_base_c.csv","w");
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
        double tempo_insertion_sort = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        fprintf(fp, "\"insertion_sort\",%d,%f\n", j, tempo_insertion_sort);
        t = clock(); 
        bubble_sort(vetor, j);
        t = clock() - t; 
        double tempo_double_sort = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        fprintf(fp, "\"bubble_sort\",%d,%f\n", j, tempo_double_sort);
        t = clock();
        selection_sort(vetor, j);
        t = clock() - t; 
        double tempo_selection_sort = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        fprintf(fp, "\"selection_sort\",%d,%f\n", j, tempo_selection_sort);
        t = clock();
        shell_sort(vetor, j);
        t = clock() - t; 
        double tempo_shell_sort = ((double)t)/CLOCKS_PER_SEC; // in seconds  
        fprintf(fp, "\"shell_sort\",%d,%f\n", j, tempo_shell_sort);
    }
    return 0; 
}