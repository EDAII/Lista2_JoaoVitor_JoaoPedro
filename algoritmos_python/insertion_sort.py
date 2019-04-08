def insertion_sort(lista):
    """
    Realiza ordenacao utilizando insertion sort
    lista: Vetor de inteiros
    """
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >=0 and key < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
        lista[j+1] = key