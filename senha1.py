nome = input("Cadastre seu nome: ")
senha = int(input("Agora cadastre sua senha: "))
senha1 = 0
nome1 = ''
arq = False
while nome != nome1 or senha != senha1 and not arq:
    nome1 = input("Agora digite nome para login: ")
    senha1 = int(input("Sua senha de autentificacao: "))
    if nome == nome1 and senha == senha1:
        arq = True
    else:
        print("Login ou senha erradas")

if arq:
    print("Bem vindo a DeepWeb")
