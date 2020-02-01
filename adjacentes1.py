entrada = n = int(input("Digita uma sequencia e numero: "))

adj = False

while entrada and not adj:
    anterior = entrada % 10
    entrada = entrada // 10
    atual = entrada % 10
    if anterior == atual:
        adj = True

if adj:
    print("Sim")
else:
    print("Nao")
