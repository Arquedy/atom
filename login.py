import pymysql
import time

class Logon:
    def conexao():

        login(resultado)

    def login(self):
        bd = pymysql.connect(host = 'localhost',
                             user = 'samuel',
                             password = '93254107',
                             db = 'Dados',
                             charset = 'utf8mb4',
                             unix_socket = '/var/run/mysqld/mysqld.sock',
                             cursorclass = pymysql.cursors.DictCursor)

        cursor = bd.cursor()
        sql = """select * from usuarios"""
        cursor.execute(sql)
        resultado = cursor.fetchall() para leitura
        #bd.commit() para inserir cadastrados
        #bd.close() fecha os dados
        login = self.email_entry.get()
        senha = self.senha_entry.get()
        for i in resultado:
            if nome == i['nome'] and senha == i['senha']:
                if i['nivel'] == 1:
                    usuarioMaster = True
                elif i['nivel'] == 2:
                    usuarioMaster == False
                usuarioAtenticado = True
                if usuarioAtenticado and usuarioMaster:
                    print('Procurando e identificando usuario')
                    loginShearch = 'Procurando e indentificando usuario'
                    self.labelVar.set(loginShearch)
                    time.sleep(5)
                    print('Usuario root logado, tenha cuidado')
                    loginRight = 'Usuario root logado com sucesso'
                    self.labelVar.set(loginRight)

                elif usuarioAtenticado and not usuarioMaster:
                    print('Usuario comum, opçoes limitadas')
                    loginHost = 'Logado'
                    self.labelVar.set(loginHost)

                break
            else:
                usuarioAtenticado = False

        if not usuarioAtenticado:
            print('Usuario teve um erro')
            erro = 'E-mail ou senha errado'
            self.labelVar.set(erro)
