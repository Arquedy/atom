tamanho = int(input("Defina a quantidade de numeros que vai ser multiplicado: "))

produto = 1
repeticao = 0

while repeticao < tamanho:
    valor = int(input("Digite o/os numero: "))
    produto = produto * valor
    repeticao = repeticao + 1

print("O valor dos produtos são: ", produto)
