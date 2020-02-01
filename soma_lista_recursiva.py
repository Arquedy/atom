def  soma_lista(lista):

    if (len(lista) == 1):
        return lista[0]
    else:
        a = lista[1:]
        valor = lista[0] + soma_lista(a)

    return valor

a = [1,2,3,4,5,6]
soma_lista(a)
