import matplotlib.pyplot as plt
import pandas as pd
import csv

def gera_csv_resultado(tempo_ordenacao, nome_linguagem):
    """
    Gera csv de resultados
    tempo_ordenacao: dicionario com tempos de ordenacao dos algoritmos
    nome_linguagem: string com nome da linguagem de implementação do algoritmo
    """
    df = pd.DataFrame(tempo_ordenacao)
    nome_arquivo = 'resultados_' + nome_linguagem + '.csv'
    df.to_csv(nome_arquivo)

def plot_grafico(tempo_ordenacao, nome_linguagem):
    """
    Plota gráfico de Tempo(s) x tamanho vetor por algoritmos de uma determinada linguagem
    tempo_ordenacao: dicionario com tempos de ordenacao dos algoritmos
    nome_linguagem: string com nome da linguagem de implementação do algoritmo
    """
    pd.DataFrame(tempo_ordenacao).plot(kind='line')
    titulo_grafico = 'Grafico Tempo(s) x Tamanho vetor em ' + nome_linguagem
    plt.title(titulo_grafico)
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    plt.show()

def compara_python_c(tempo_python, tempo_c):
    """
    Plota dois gráficos de Tempo(s) x tamanho vetor por algoritmos em c e python
    tempo_python: dicionario com tempos de ordenacao dos algoritmos em python
    tempo_c: dicionario com tempos de ordenacao dos algoritmos em c
    """
    pd.DataFrame(tempo_python).plot(kind='line')
    plt.title('Grafico Tempo(s) x Tamanho vetor: Python')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    pd.DataFrame(tempo_c).plot(kind='line')
    plt.title('Grafico Tempo(s) x Tamanho vetor: C')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    plt.show()