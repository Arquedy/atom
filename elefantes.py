def  incomodam(n):
    '''devolve uma string contendo "incomodam " n vezes para o refrão. Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia utilizando recursão'''
    if ( n <= 0):
        return ""
    else:
        return "incomodam " + incomodam(n-1)


def monta_frases(n):
    if (n == 2):
        frase = "Um elefante incomoda muita gente \n2 elefantes incomodam incomodam muito mais "
    else:
        frase = "\n{0} elefantes incomodam muita gente \n{1} elefantes {2}muito mais".format(n-1, n, incomodam(n))

    return frase

def elefantes(n):
    '''  devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia utilizando recursão'''
    if ( n <= 1):
        return ""
    else:
        return elefantes(n-1) + monta_frases(n)
