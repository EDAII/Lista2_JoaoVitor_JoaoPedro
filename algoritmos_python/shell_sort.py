def shell_sort(lista):
    h = 1
    n = len(lista)
    while h > 0:
            for i in range(h, n):
                c = lista[i]
                j = i
                while j >= h and c < lista[j - h]:
                    lista[j] = lista[j - h]
                    j = j - h
                    lista[j] = c
            h = int(h / 2.2)