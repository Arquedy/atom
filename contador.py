num = int(input("Digite um numero inteiro: "))
n = num

#i ira ser o contador
i = 0
# duv sera o numero dividido
div = 0
#precisei colocar o seg para parae p while quando o valor inserido for 0
seg = True
while n >= 0 and seg:
    div = n % 10
    i = i + div
    n = n // 10
    if n == 0:
      seg = False

print(i)
