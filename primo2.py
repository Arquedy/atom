from tkinter import *
from tkinter import messagebox
import pymysql

class SQL:
    def __init__(self):
        self.windows = Tk()
        self.windows.title('Cadastro')
        self.frame1 = Frame(self.windows)
        self.label1 = Label(self.frame1, text = 'Dados prontos para serem inseridos')
        self.entrada1 = Entry(self.frame1, width = 30)
        self.entrada2 = Entry(self.frame1, width = 30)
        self.entrada3 = Entry(self.frame1, width = 30)
        self.entrada4 = Entry(self.frame1, width = 30)
        self.entrada5 = Entry(self.frame1, width = 30)
        self.entrada6 = Entry(self.frame1, width = 30)

        self.label1.pack(side = 'left')
        self.entrada1.pack(side = 'left')
        self.entrada2.pack(side = 'left')
        self.entrada3.pack(side = 'left')
        self.entrada4.pack(side = 'left')
        self.entrada5.pack(side = 'left')
        self.entrada6.pack(side = 'left')

        self.frame2 = Frame(self.windows)
        self.label2_dinamica = StringVar
        self.label2 = Label(self.frame2, textvariable = self.label2_dinamica)
        self.label2.pack(side = 'left')

        self.frame3 = Frame(self.windows)
        self.botao = Button(self.frame3, text = 'Cadastrar', command = self.cadastro)
        self.encerrar = Button(self.frame3, text - 'Sair', command = self.quit)
        self.botao.pack(side = 'left')
        self.encerrar.pack(side = 'left')

        self.frame.pack()
        self.frame2.pack()
        self.frame3.pack()

        mainloop()

    def cadastro(self):
        bd = pymysql.connect(host = 'localhost',
                             user = 'samuel',
                             password = '93254107',
                             db = 'EMPRESAS',
                             charset = 'utf8mb4',
                             unix_socket = '/var/run/mysqld/mysqld.sock',
                             cursorclass = pymysql.cursors.DictCursor)

        cursor = bd.cursor()

        try:
            nome = input("Empresa: ")
            url = input("Site: ")
            contato = input("Seu nome: ")
            telefone = input("Seu telefone: ")
            cnpj = input("CNPJ da empresa: ")
            email = input("Por ultimo, se email:")
            sql = """INSERT INTO fornecedores(nome, url, contato, telefone, cnpj, email) VALUES ('{}','{}','{}','{}','{}','{}')""".format(nome, url, contato, telefone, cnpj, email)
            cursor.execute(sql)
            print("Dados incluidos com sucesso")
            bd.commit()
            time.sleep(5)

        except:
            bd.rollback()
            print("Erro na insercao de dados na tabela de fornecedores")


        # fecha a conexão
        bd.close()

        return 0

if __name__ == '__main__':
     import sys
     sys.exit(main(sys.argv))
