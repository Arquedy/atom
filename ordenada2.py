class Eficiente:
    def facil(self, lista2):
        lista_comparacao = lista2[:]
        lista_comparacao.sort()
        if lista_comparacao == lista2:
            return True
        else:
            return False
