import pymysql

bd = pymysql.connect(host = 'localhost',
                     user = 'samuel',
                     password = '93254107',
                     db = 'erp',
                     charset = 'utf8mb4',
                     unix_socket = '/var/run/mysqld/mysqld.sock',
                     cursorclass = pymysql.cursors.DictCursor)

cursor = bd.cursor()

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('Digite seu nome ')
        senha = input('Digite sua senha ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        if not autenticado:
            print('Email ou Senha incorreto')

    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('Qual o nome de login: ')
        senha = input('Qual a senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1

        if usuarioExistente == 1:
                print('Usuario ja existe, por favor entre coom um novo Usuario')
        elif usuarioExistente == 0:
            try:
                sql1 = """insert into cadastros (nome, senha, nivel) values ('{}', '{}', 1)""".format(nome, senha)

                cursor.execute(sql1)
                bd.commit()
                print('Usuario cadastrado com sucesso')

            except:
                print('Erro ao inserir os dados')
    return autenticado, usuarioMaster

def excluirProdutos():
    idProduto = int(input('Digite o id do produto que deseja apagar: '))
    try:
        sql2 = """delete from produtos where id = {}""".format(idProduto)
        cursor.execute(sql2)
        print('Excluido')
    except:
        print('Nao foi possivel excluir')

def listarPedidos():
    pedidos = []
    escolha = 0
    while escolha != 2:
        pedidos.clear()
        try:
            sql = """select * from pedidos"""
            cursor.execute(sql)
            listarPedidos = cursor.fetchall()
        except:
            ('Erro, contate o administrador')

        for i in listarPedidos:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(0, len(


            pedidos)):
                print(pedidos[i])

        else:
            print('Nenhum pedido, relaxe')

        escolha = int(input('Escolha 1 para dar pedido como entregar ou 2 para voltar: '))
        if escolha == 1:
            idEntrega = int(input('Qual o id do produto que esta pronto: '))
            try:
                sql3 = """delete from pedidos where id = {}""".format(idEntrega)
                cursor.execute(sql3)
                print('Entregue')
            except:
                print('Nao foi possivel excluir')

def gerarEstastiticas():
    nomeProdutos = []
    nomeProdutos.clear()
    try:
        sql3 = """select * from produtos"""
        elementos = cursor.fetchall(sql3)

        print('Usuario cadastrado com sucesso')

    except:
        print('Erro ao fazer a consulta')

    try:
        sql4 = """select * from estatisticasVendido"""
        vendidos = cursor.fetchall(sql4)

    except:
        print('erro ao consultar banco de dados')

    estado = int(input('digite 0 para sair, 1 para pesquisar por nome, 2 para pesquisar por grupo'))
    if estado == 1:
        decisao3 = int(input('Digite 1 para pesquisar por dinherio e 2 por quantidade unitaria'))
        if decisao3 == 1:
            for i in elementos:
                nomeProdutos.append(i['nome'])
            valores = []
            valores.clear()
            


def listarProdutos():
    try:
        sql = """select * from produtos"""
        cursor.execute(sql)
        produtosCadastrados = cursor.fetchall()

    except:
        print('Erro ao buscar dados')

    cont = 0

    for i in range(len(produtosCadastrados)):
        print('O id do produto: ', produtosCadastrados[cont]['id'])
        print('Nome ', produtosCadastrados[cont]['nome'])
        print('ingredientes ', produtosCadastrados[cont]['ingredientes'])
        print('Grupo ', produtosCadastrados[cont]['grupo'])
        print('Preço ', produtosCadastrados[cont]['preco'])
        print('-----------------------------')
        cont = cont + 1

def cadastrarProdutos():
    nome = input('Digite o nome do produto: ')
    ingredientes = input('Digite os ingredientes dos produtos: ')
    grupo = input('Digite o grupo pertecente a esse produto: ')
    preco = float(input('Digite o preçp do produto'))

    try:
        sql1 = """insert into produtos (nome, ingredientes, grupo, preco) values ('{}', '{}', '{}', {})""".format(nome, ingredientes, grupo, preco)

        cursor.execute(sql1)
        bd.commit()
        print('Produto cadastrado com sucesso')

    except:
        print('Nao foi possivel inserir os produtos')

autentico = False
while not autentico:
    decisao = int(input('Digite 1 para logar ou digite 2 para cadastrar: '))
    try:
        sql = """select * from cadastros"""
        cursor.execute(sql)
        resultado = cursor.fetchall()

    except:
        print('Erro ao conectar ao banco de dados')
    autentico, usuarioSupremo = logarCadastrar()

if autentico == True:
    print('autenticado')
    if usuarioSupremo == True:
        decisaoUsuario = 1

        while decisaoUsuario != 0 :
            decisaoUsuario = int(input('Digite 0 para sair, 1 para cadastrar produtos, 2 para listar produtos cadastrados, 3 para listar pedido'))
            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('Digite 1 para excluir um produto ou 2 para sair: '))
                if delete == 1:
                    excluirProdutos()
            elif decisaoUsuario == 3:
                listarPedidos()

    else:
        print('Voce nao tem acesso privilegiado para cadastrar')
