print("Vou te falar a sua idade")
ano1 = input("Qual o ano atual? ")
ano2 = input("Agora qual o ano que vc nasceu? ")
atual = float(ano1)
nasceu = float(ano2)
idade = atual - nasceu

if idade <= 25:
    print("Voce tem", idade, "Ta novo, viva a vida")

else:
    print("Voce tem", idade, "Cara procura logo um medico, ta ficando velho")
