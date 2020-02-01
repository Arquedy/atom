descrescente = True
anterior = int(input("Digite o primeiro numero da sequencia: "))

valor = 1

while valor != 0 and descrescente:
    valor = int(input("Digite o proximo numero da sequencia: "))
    if valor > anterior:
       descrescente = False

if descrescente:
    print("A sequencia esta descrescente!!")
else:
    print("A sequecia não esta descrescente!!!")
