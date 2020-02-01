print("Voce tera que adicionar ate 7 pessoas, se quiser parar antes digite 0, quando perguntar o peso")
n_pessoas = 0
pessoas = {}
media = 0

while n_pessoas <= 7:
    peso = int(input("Qual o peso da pessoa?: "))
    if peso == 0:
        break
    nome = input("Qual o nome da pessoa?: ")
    pessoas[peso] = nome
    n_pessoas = n_pessoas + 1

for i in pessoas:#Se eu quiser pegar logo o valor eu colocaria pessoas.values()
    if i > 90:
        print(pessoas[i], "pesa mais que uma arroba")

for j in pessoas:
    media = j + media
final_media = media / n_pessoas
print('A media eh', final_media, 'Kilos')
