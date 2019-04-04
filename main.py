import sys
import os
pasta_atual = os.getcwd()
sys.path.insert(0, str(pasta_atual) + '/algoritmos_python')
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from gera_relatorio import gera_csv_resultado, plot_grafico, compara_python_c
from utils import insere_randomico
import time
import random
import pandas as pd
import subprocess


def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Comparacao bubble sort, insertion sort, selection sort e shell sort em python")
    print("2. Comparacao bubble sort, insertion sort, selection sort e shell sort em C")
    print("3. Compara tempos dos algoritmos em C e python")
    print("4. Gera csv com relatório dos tempos de ordenação em python")
    print("5. Gera csv com relatório dos tempos de ordenação em C")
    print("6. Sair")
    print(67 * "-")
  
def pega_resultado_c():
    df = pd.read_csv(pasta_atual + '/csv_base_c.csv', names=['algoritmo', 'tam_vetor', 'tempo_execucao'])    
    tempo_ordenacao_c = {'insertion_sort': {100: 0, 200: 0,
                  300: 0, 400: 0, 500: 0, 600: 0,
                  700: 0, 800: 0, 900: 0, 1000: 0},
                  'selection_sort':{}, 'bubble_sort': {},
                  'shell_sort': {} }
    tempo_ordenacao_c['selection_sort'].update(tempo_ordenacao_c['insertion_sort'])
    tempo_ordenacao_c['bubble_sort'].update(tempo_ordenacao_c['insertion_sort'])
    tempo_ordenacao_c['shell_sort'].update(tempo_ordenacao_c['insertion_sort'])    
    for index, row in df.iterrows():
        tempo_ordenacao_c[row['algoritmo']][row['tam_vetor']] = row['tempo_execucao']

    return tempo_ordenacao_c

def seleciona_algoritmo(algoritmo, lista, tempo_ordenacao, nome_algoritmo):
    for i in range(100,1100, 100):
        inicio_cronometagem = time.time()
        algoritmo(lista) 
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_ordenacao[nome_algoritmo][i] = tempo_cronometragem
        insere_randomico(lista, 100)    

if __name__ == '__main__':
    loop=True
    tempo_ordenacao_python = {'insertion_sort': {100: 0, 200: 0,
                  300: 0, 400: 0, 500: 0, 600: 0,
                  700: 0, 800: 0, 900: 0, 1000: 0},
                  'selection_sort':{}, 'bubble_sort': {},
                  'shell_sort': {} }
    tempo_ordenacao_python['selection_sort'].update(tempo_ordenacao_python['insertion_sort'])
    tempo_ordenacao_python['bubble_sort'].update(tempo_ordenacao_python['insertion_sort'])
    tempo_ordenacao_python['shell_sort'].update(tempo_ordenacao_python['insertion_sort'])
    tamanho_vetor = 100
    

    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-6]: ")
        if choice=='1':     
            print("Opcao 1 foi escolhida")
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(insertion_sort, lista, tempo_ordenacao_python, 'insertion_sort')
            seleciona_algoritmo(bubble_sort, lista, tempo_ordenacao_python, 'bubble_sort')
            seleciona_algoritmo(selection_sort, lista, tempo_ordenacao_python, 'selection_sort')
            seleciona_algoritmo(shell_sort, lista, tempo_ordenacao_python, 'shell_sort')
            plot_grafico(tempo_ordenacao_python, 'python')
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            subprocess.call(['./executa_prog.sh'])
            tempo_ordenacao_c = pega_resultado_c()
            plot_grafico(tempo_ordenacao_c, 'c')           
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            subprocess.call(['./executa_prog.sh'])
            tempo_ordenacao_c = pega_resultado_c()
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(insertion_sort, lista, tempo_ordenacao_python, 'insertion_sort')
            seleciona_algoritmo(bubble_sort, lista, tempo_ordenacao_python, 'bubble_sort')
            seleciona_algoritmo(selection_sort, lista, tempo_ordenacao_python, 'selection_sort')
            seleciona_algoritmo(shell_sort, lista, tempo_ordenacao_python, 'shell_sort')
            compara_python_c(tempo_ordenacao_python, tempo_ordenacao_c)
        elif choice=='4':
            print("Opcao 4 foi escolhida")
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(insertion_sort, lista, tempo_ordenacao_python, 'insertion_sort')
            seleciona_algoritmo(bubble_sort, lista, tempo_ordenacao_python, 'bubble_sort')
            seleciona_algoritmo(selection_sort, lista, tempo_ordenacao_python, 'selection_sort')
            seleciona_algoritmo(shell_sort, lista, tempo_ordenacao_python, 'shell_sort')
            gera_csv_resultado(tempo_ordenacao_python, 'python')
        elif choice=='5':
            print("Opcao 5 foi escolhida")
            subprocess.call(['./executa_prog.sh'])
            gera_csv_resultado(tempo_ordenacao_c, 'C')        
        elif choice=='6':
            print("Opcao 6 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")    
    gera_csv_resultado(tempo_ordenacao_python, 'python')
    
    
    
