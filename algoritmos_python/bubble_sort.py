def bubble_sort(lista):
    """
    Realiza ordenacao utilizando bubble sort
    lista: Vetor de inteiros
    """    
    tamanho_vetor = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(tamanho_vetor):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False