from tqdm import tqdm
import time
dados = [{'Nome' : 'Samuel', 'Idade' : 28, 'Telefone' : 989253996, 'CPF' : 37550566828}, {'Nome' : 'Nilda', 'Idade' : 61, 'Telefone' : 994073398, 'CPF' : 2463375833}]
x = len(dados)
print('Foram encontrados {}, enderecos'.format(x))
print('Inserindo dados, o sistema pode sofrer um pouco de lentidao')
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
cont = 0
for i in tqdm(range(x)):
    cidade = dados[cont]['Nome']
    endereco = dados[cont]['Idade']
    nome = dados[cont]['Telefone']
    seguimento = dados[cont]['CPF']
    cont = cont + 1

    time.speed(0.2)
