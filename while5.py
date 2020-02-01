meuCartao = int(input("Digite o numero do seu cartao: "))

cartaoLido = 1
encontreiMeu = False

while cartaoLido != 0 and not encontreiMeu:
    cartaoLido = int(input("Digite o numero do proximo cartao: "))
    if cartaoLido == meuCartao:
        encontreiMeu = True
