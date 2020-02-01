import ordenada
import ordenada2
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(5000)#essa função fera inteiros aleatorios de 0 a 999
        return lista

    def compara(self, n):
        lista = self.lista_aleatoria(n)
        lista2 = lista[:]

        o = ordenada.Ordenador()

        antes1 = time.time()
        o.ordenada(lista)
        depois1 = time.time()
        conta1 = depois1 - antes1

        print("A ordenada demorou",conta1, "segundos.")

        e = ordenada2.Eficiente()

        antes2 = time.time()
        e.facil(lista2)
        depois2 = time.time()
        conta2 = depois2 - antes2

        print("O algoritimo q eu eu julgo eficiente demorou", conta2,"segundos.")
        if conta1 < conta2:
            print("O ordenada é mais eficiente")
        else:
            print("O ordenada2 é mais eficiente")
        

c = ContaTempos()
c.compara(1000)
