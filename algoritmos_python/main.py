from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from gera_relatorio import gera_csv, plot_grafico
import time
import random
import utils

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Comparacao bubble sort e insertion sort")
    # print("2. Realizar buscas e insercoes. Sendo as buscas realizadas na metade dos vetores e listas encadeadas")
    # print("3. Realizar buscas(20%), insercoes(40%) e remocoes(40%) aleatoriamente")
    print("4. Sair")
    print(67 * "-")
  
def seleciona_algoritmo(algoritmo, lista, tempo_ordenacao, nome_algoritmo):
    for i in range(100,1100, 100):
        inicio_cronometagem = time.time()
        algoritmo(lista) 
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_ordenacao[nome_algoritmo][i] = tempo_cronometragem
        utils.insere_randomico(lista, 100)
    


if __name__ == '__main__':
    loop=True
    tempo_ordenacao = {'insertion_sort': {100: 0, 200: 0,
                  300: 0, 400: 0, 500: 0, 600: 0,
                  700: 0, 800: 0, 900: 0, 1000: 0},
                  'selection_sort':{}, 'bubble_sort': {},
                  'shell_sort': {} }
    tempo_ordenacao['selection_sort'].update(tempo_ordenacao['insertion_sort'])
    tempo_ordenacao['bubble_sort'].update(tempo_ordenacao['insertion_sort'])
    tempo_ordenacao['shell_sort'].update(tempo_ordenacao['insertion_sort'])
    tamanho_vetor = 100
    lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)

    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-4]: ")
        if choice=='1':     
            print("Opcao 1 foi escolhida")
            seleciona_algoritmo(insertion_sort, lista, tempo_ordenacao, 'insertion_sort')
            seleciona_algoritmo(bubble_sort, lista, tempo_ordenacao, 'bubble_sort')
            seleciona_algoritmo(selection_sort, lista, tempo_ordenacao, 'selection_sort')
            seleciona_algoritmo(shell_sort, lista, tempo_ordenacao, 'shell_sort')
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            # busca_media.main()
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            # insercao_aleatoria.main()
        elif choice=='4':
            print("Opcao 4 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")
    print(tempo_ordenacao)
    gera_csv(tempo_ordenacao)
    plot_grafico(tempo_ordenacao)

