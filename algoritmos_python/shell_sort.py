def shell_sort(lista):
    """
    Realiza ordenacao utilizando bubble sort
    lista: Vetor de inteiros
    """
    h = 1
    tam_vetor = len(lista)
    while h > 0:
            for i in range(h, tam_vetor):
                c = lista[i]
                j = i
                while j >= h and c < lista[j - h]:
                    lista[j] = lista[j - h]
                    j = j - h
                    lista[j] = c
            h = int(h / 2.2)