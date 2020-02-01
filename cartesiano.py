import math

num1 = input("Insira o x1: ")
num2 = input("Insira o y1: ")
num3 = input("Insira o x2: ")
num4 = input("Insira o y2: ")

x1 = float(num1)
y1 = float(num2)
x2 = float(num3)
y2 = float(num4)

xis = (x1 - x2)**2
yis = (y1 - y2)**2
soma = xis + yis
raiz = math.sqrt(soma)

if raiz >= 10:
    print("Longe")

else:
    print("Perto")
