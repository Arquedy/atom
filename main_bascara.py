from treino_classes import Baskara
import math
primeiro = float(input("Entra com a: "))
segundo = float(input("Entre com b: "))
terceiro = float(input("Entre com c:"))

result = Baskara(primeiro, segundo, terceiro)

print(result.resultado())
