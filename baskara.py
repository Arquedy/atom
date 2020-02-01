print("Voce vai colocar as tres variaveis para calculo")
print("Por favor, isso eh um programa e nao humano, se se nao tiver variavel, coloca o numero 0, NAO SEJA BURRO")
print("Outra coisa, se o programa voltar com algum 0, entao ele so tem uma raiz, não considerar o 0")
import math

ax = input("Entre com o valor de ax² ")
bx = input("Entre agora com o bx ")
cx = input("Só falta o c ")

#vou converter as strings em float
a = float(ax)
b = float(bx)
c = float(cx)
#eu sei que poderia ter feito isso la em cima de forma mais simples, mas PNC

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
