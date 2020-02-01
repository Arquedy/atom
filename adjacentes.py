entrada = n = int(input("Digita uma sequencia e numero: "))

adj = False

while entrada and not adj:
    anterior = entrada % 10
    entrada = entrada // 10
    atual = entrada % 10
    if anterior == atual:
        adj = True

if adj:
    print(n, "tem dois numero", atual, "Iguais!!!!!!")
else:
    print("Voce ns prestou atenção neh kkkk, tem nada igual ae n")
