import matplotlib.pyplot as plt
import pandas as pd

def gera_csv(dicionario):
    df = pd.DataFrame(dicionario)
    df.to_csv('relatorio.csv')

def plot_grafico(dicionario):
    pd.DataFrame(dicionario).plot(kind='bar')
    plt.show()
    pd.DataFrame(dicionario).plot(kind='line')
    plt.show()
    pd.DataFrame(dicionario).plot(kind='barh')
    plt.show()