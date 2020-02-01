class Ordenador:
    def ordenada(self, lista):
        next = 0
        for i in range(len(lista)):
            next = i + 1
            if next < len(lista):
                if lista[i] > lista[next]:
                    return False
        return True
