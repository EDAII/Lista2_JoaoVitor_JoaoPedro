import random
import time

tempo_ordenacao = {'insertion_sort': {1000: 0, 2000: 0,
                  3000: 0, 4000: 0, 5000: 0, 6000: 0,
                  7000: 0, 8000: 0, 9000: 0, 10000: 0},
                  'quick_sort':{}, }
tempo_ordenacao['quick_sort'].update(tempo_ordenacao['insertion_sort'])


def insere_randomico(lista, qtd_insercao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_insercao -- quantidade a ser inserida na lista
    """
    for contador in range(qtd_insercao):
        lista.append(random.randint(1,qtd_insercao))
    random.shuffle(lista)
    return lista

# Function to do insertion sort
def insertionSort(lista):  
    # Traverse through 1 to len(lista) 
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >=0 and key < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
        lista[j+1] = key

tamanho_vetor = 1000

lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)

for i in range(1000,11000, 1000):
    inicio_cronometagem = time.time()
    insertionSort(lista) 
    fim_cronometragem = time.time()
    tempo_cronometragem = fim_cronometragem - inicio_cronometagem
    tempo_ordenacao['insertion_sort'][i] = tempo_cronometragem
    insere_randomico(lista, 1000)


print(tempo_ordenacao)
