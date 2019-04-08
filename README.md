# Lista 1 -  EDA2 2019-1

## João Vitor Ramos de Souza e João Pedro Soares

### Do que se trata?
O programa oferece três análises diferentes de algoritmos de ordenação.

 - A **Opção 1** uma função de comparação de algorítimos de ordenação realizados em python (bubble sort, insertion sort, selection sort e shell sort) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor inicialmente com tamanho de 1000 elementos. A cada iteração o vetor cresce em 1000 posições, no final atingindo 10000 posições. Ao final um gráfico será gerado para a execução dos algoritmos em python.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**
 
  - A **Opção 2** uma função de comparação de algorítimos de ordenação realizados em C (bubble sort, insertion sort, selection sort e shell sort) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor inicialmente com tamanho de 1000 elementos. A cada iteração o vetor cresce em 1000 posições, no final atingindo 10000 posições. Ao final um gráfico será gerado para a execução dos algoritmos em C.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**


 - A **Opção 3** uma função de comparação de algorítimos de ordenação realizados em C (bubble sort, insertion sort, selection sort e shell sort) e  algorítimos de ordenação realizados em python(bubble sort, insertion sort, selection sort e shell sort) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor inicialmente com tamanho de 1000 elementos. A cada iteração o vetor cresce em 1000 posições, no final atingindo 10000 posições. Ao final dois gráficos serão gerados, um para a execução dos algoritmos em python e o outro para a execução dos algoritmos em C.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**

  - A **Opção 4** uma função de comparação de algorítimos de ordenação realizados em C (bubble sort, insertion sort, selection sort e shell sort) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor inicialmente com tamanho de 1000 elementos. A cada iteração o vetor cresce em 1000 posições, no final atingindo 10000 posições. Ao final um gráfico será gerado um csv como relatório da  execução dos algoritmos em python.
 **AVISO: Esta função demora alguns segundos para completar. O csv será gerado ao final da execução**

  - A **Opção 5** uma função de comparação de algorítimos de ordenação realizados em C (bubble sort, insertion sort, selection sort e shell sort) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor inicialmente com tamanho de 1000 elementos. A cada iteração o vetor cresce em 1000 posições, no final atingindo 10000 posições. Ao final um gráfico será gerado um csv como relatório da  execução dos algoritmos em C.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**


- A **Opção 6** é apenas a opção para sair do programa.


### Utilizando
#### Pré requisitos
Antes de utilizar o programa, você precisará do `matplotlib`, `python3-tk`, `pandas` e `gcc`.

Em distribuições que utilizam o gerenciador de pacotes `apt`, utilize:

    $ sudo apt-get update
    $ sudo apt-get install pip3
    $ sudo apt-get install python3-tk 
    $ pip3 install matplotlib
    $ pip3 install pandas
    
#### Executando
Após o passo anterior, para executar o programa, navegue até o diretório raiz do programa e utilize:

    $ python3 main.py

Caso ocorra algum erro de execução nas funções relacionadas aos algoritmos em c, realize o seguinte comando, pode ocorrer por ser um shell script e n possuir alterações para a sua execução: 

    $ chmod +x executa_prog.sh

**Observação: Durante a execução do programa um arquivo csv com o nome "csv_base_c.csv" será gerado para posterior geração de gráficos e csv's**

 
