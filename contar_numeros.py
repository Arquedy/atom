n = int(input("Entre com um numero qualque:"))
somador = 0
integrador = 0
while n > 0:
    somador = n % 10
    integrador = integrador + somador
    n = n // 10
print(integrador)
