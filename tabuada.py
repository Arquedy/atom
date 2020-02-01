print(
"Esta programa visa fazer tabuada de acordo com o pedido"
)

tab = int(input(
"Digite o numero da tabuada que deseja saber?: "
))

i = 0
num = 0
while i <= 10:
    num = tab * i
    print( tab, "x", i, "=", num)
    i = i + 1
