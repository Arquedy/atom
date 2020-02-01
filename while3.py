numero = int(input("Digita um numero que eu vou soma-lo: "))
soma = 0

while numero > 0:
    soma = soma + (numero % 10)
    numero = numero // 10


print(soma)
