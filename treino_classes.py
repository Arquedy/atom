import math

class Baskara:

    def __init__(self, a, b, c):
        self.ax = float(a)
        self.bx = float(b)
        self.cx = float(c)

    def resultado(self):
        import math
        a = self.ax
        b = self.bx
        c = self.cx

        #operações Agora
        delta = b ** 2 - 4 * a * c
        multiA = 2 * a
        #importa função math


        #comando IF Agora
        if delta < 0:
            print("Não sei aonde vc arrumou essa equação, mas ela n tem raiz ")


        elif delta == 0:
            raiz = math.sqrt(delta)
            x1 = (-b + raiz)/multiA
            x2 = (-b - raiz)/multiA
            print("Tem uma raiz que é: ", x1)

        elif delta > 0:
            raiz = math.sqrt(delta)
            x1 = (-b + raiz)/multiA
            x2 = (-b - raiz)/multiA
            print("Boa, tem duas raizes que é: ", x1, x2)
