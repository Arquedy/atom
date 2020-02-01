cpf = int(input('Entre com seu CPF: '))
lista = []
n = cpf
tirar = 0
lista2 = []
lista3 = []
soma = 0
coofator = [1,1,1,4,4,4,7,7,7]

for i in (0, 1):
    n = n // 10

while n > 0:
    tirar = n % 10
    lista.append(tirar)
    n = n //10

for i in range( len(lista)-1, -1, -1):
    lista2.append(lista[i])

print(lista2)

for i in range(len(lista2)):
            multi = coofator[i] * lista2[i]
            lista3.append(multi)

print(lista3)

for j in range(len(lista3)):
    soma = soma + lista3[j]
    print(soma)

result = soma % 11
print(result)
verifica_digito1 = 11 - result
print(verifica_digito1)
