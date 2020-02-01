print("Programa para receita liquido")
salario = float(input("Digite quanto voce ganha por hora: "))
horas = float(input("E quantas horas voce trabalha ao mes?: "))
bruto = salario * horas
if bruto >= 2500:
    IR = (bruto * 11) / 100
else:
    IR = 0
        
INSS = (bruto * 8) / 100
SIN = (bruto * 5) / 100
SAL = bruto - IR - INSS - SIN
#Brasileiro ta no sal mesmo
print("+ Salario Bruto: ",bruto)
print("- IR (11%): ",IR)
print("- INSS (8%): ",INSS)
print("- Sindicato (5%): ",SIN)
print("= Salario Liquido: ",SAL)
