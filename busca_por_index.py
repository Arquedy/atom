def busca(lista, elemento):

    first = 0
    last = len(lista) - 1

    while first <= last:
        i = int((first + last) / 2)
        print(i)
        if lista[i] == elemento:
            return i
        elif lista[i] > elemento:
            last = i - 1
        elif lista[i] < elemento:
            first = i + 1
        else:
            return False

    return False
