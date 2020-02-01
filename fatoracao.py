num = int(input(" Digite um numero inteiro para ser fatorado: "))
c = num
f = 1

while c > 0:
    f = f * c
    c = c - 1

print(f)
