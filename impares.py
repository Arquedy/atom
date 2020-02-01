n = int(input("Entre com um numero: "))
cont = 0
impar = 1
while cont <= n:
    impar = cont % 2
    if impar != 0:
        print(cont)
    cont = cont + 1
