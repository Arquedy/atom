num = n = int(input(" Digite um numero, pode ser quantas casas quiser: "))
t = False

while n > 0 and t == False:
    entrada = n % 10
    n = n // 10
    atual = n % 10
    if entrada == atual:
        t = True

if t:
    print("O numero", num, "tem o numero", atual, "repetido")

else:
    print("O numero", num, "nao tem numeros repetidos")
