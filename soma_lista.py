def soma_lista(lista):
    soma = 0 #ira ser o que vai somar
    pegador = 0 #o que ira pegar cada valor da lista
    for i in range(len(lista)):
        pegador = lista[i]
        soma = soma + pegador
    print(soma)
