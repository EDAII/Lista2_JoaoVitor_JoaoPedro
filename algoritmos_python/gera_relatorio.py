import matplotlib.pyplot as plt
import pandas as pd
import csv

def gera_csv_resultado(dicionario, nome_linguagem):
    df = pd.DataFrame(dicionario)
    nome_arquivo = 'resultados_' + nome_linguagem + '.csv'
    df.to_csv(nome_arquivo)

def plot_grafico(dicionario, nome_linguagem):
    pd.DataFrame(dicionario).plot(kind='line')
    titulo_grafico = 'Grafico Tempo(s) x Tamanho vetor em ' + nome_linguagem
    plt.title(titulo_grafico)
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    plt.show()

def compara_python_c(tempo_python, tempo_c):
    pd.DataFrame(tempo_python).plot(kind='line')
    plt.title('Grafico Tempo(s) x Tamanho vetor: Python')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    pd.DataFrame(tempo_c).plot(kind='line')
    plt.title('Grafico Tempo(s) x Tamanho vetor: C')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    plt.show()