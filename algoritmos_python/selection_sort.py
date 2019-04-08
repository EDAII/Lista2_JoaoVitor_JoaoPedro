def selection_sort(lista):
    """
    Realiza ordenacao utilizando selection sort
    lista: Vetor de inteiros
    """
    for index in range(0, len(lista)):
        min_index = index

        for right in range(index + 1, len(lista)):
            if lista[right] < lista[min_index]:
                min_index = right

        lista[index], lista[min_index] = lista[min_index], lista[index]