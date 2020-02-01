from tkinter import *
from tkinter import messagebox
import pymysql

class Visualizar:
    def __init__(self):
        self.windows3 = Tk()
        self.windows.title3('Alteração de dados')
        self.frame6 = Frame(self.windows3)
        self.label7 = Label(self.frame6, text = 'Nao sera possivel alterar o nome, tao pouco o CNPJ')

        self.frame7 = Frame(self.windows3)
        self.label8 = Label(self.frame7, text = 'Qual o CNPJ da empresa?')
        self.entradaCNPJ = Entry(self.frame7, width = 25)

        self.label7.pack(side = 'top')
        self.label8.pack(side = 'left')
        self.entradaCNPJ.pack(side = 'left')

        self.frame101 = Frame(self.windows3)
        self.botao = Button(self.frame101, text = 'Buscar', command = self.buscar)
        self.botao1 = Button(self.frame101, text = 'Alterar', command = self.alterar)
        self.sair = Button(self.frame101, text = 'Sair', command = self.feche)

        self.frame111 = Frame(self.windows3)
        self.labelERRO = StringVar()
        self.label10 = Label(self.frame111, textvariable = self.labelERRO)

        self.label10.pack(anchor = 'center')

        self.botao.pack(side = 'left')
        self.botao1.pack(side = 'left')
        self.sair.pack(side = 'left')

        self.frame6.pack()
        self.frame7.pack()
        self.frame101.pack()
        self.frame111.pack()

        mainloop()

    def buscar(self):
        bd = pymysql.connect(host = 'localhost',
                             user = 'samuel',
                             password = '93254107',
                             db = 'EMPRESAS',
                             charset = 'utf8mb4',
                             unix_socket = '/var/run/mysqld/mysqld.sock',
                             cursorclass = pymysql.cursors.DictCursor)

        cursor = bd.cursor()
        con = self.entradaCNPJ.get()
        result = """SELECT url, telefone, email FROM fornecedores WHERE cnpj = '{}'""".format(con)

        try:
            # Execute o comando SQL
            cursor.execute(result)
            # le todas as linhas da tabela.
            linhas = cursor.fetchall()

            #print (linhas)

            for linha in linhas:
                urlx = linha['url']
                telefoneX = linha['telefone']
                emailX= linha['email']


        except:
            erro = 'Erro ao consultar dados, contate o administrador'
            self.labelERRO.set(erro)

        try:

            self.frame8 = Frame(self.windows3)
            self.labelURL = Label(self.frame8, text = 'Qual o novo URL: ')
            self.entradaURL = Entry(self.frame8, width = 25)
            self.entradaURL.insert(index = 0, string = '{}'.format(urlx))
            self.frame9 = Frame(self.windows3)
            self.labelTEL = Label(self.frame9, text = 'Qual o novo telefone: ')
            self.entradaTEL = Entry(self.frame9, width = 25)
            self.entradaTEL.insert(index = 0, string = '{}'.format(telefoneX))

            self.frame10 = Frame(self.windows3)
            self.labelE = Label(self.frame10, text = 'Qual o novo e-mail: ')
            self.entradaE = Entry(self.frame10, width = 25)
            self.entradaE.insert(index = 0, string = '{}'.format(emailX))

            self.labelURL.pack(side = 'left')
            self.entradaURL.pack(side = 'left')
            self.labelTEL.pack(side = 'left')
            self.entradaTEL.pack(side = 'left')
            self.labelE.pack(side = 'left')
            self.entradaE.pack(side = 'left')

            self.frame8.pack()
            self.frame9.pack()
            self.frame10.pack()

            bd.close()
            messagebox.showinfo('Alerta', 'Os dados forram atualizados com sucesso')




        except:
            erro = 'Erro ao consultar dados, contate o administrador'
            self.labelERRO.set(erro)

    def alterar(self):
        try:
            bd = pymysql.connect(host = 'localhost',
                                 user = 'samuel',
                                 password = '93254107',
                                 db = 'EMPRESAS',
                                 charset = 'utf8mb4',
                                 unix_socket = '/var/run/mysqld/mysqld.sock',
                                 cursorclass = pymysql.cursors.DictCursor)

            cursor = bd.cursor()
            cone = self.entradaCNPJ.get()
            cone1 = self.entradaURL.get()
            cone2 = self.entradaTEL.get()
            cone3 = self.entradaE.get()

            result1 = "UPDATE fornecedores SET url = '{}', telefone = {}, email = '{}' WHERE cnpj = {}".format(cone1, cone2, cone3, cone)
            cursor.execute(result1)
            bd.commit()
            bd.close()


        except:
            messagebox.showinfo('ERRO', 'Os dados nao foram alterados por segurança')


    def feche(self):
            quit()

minha = Visualizar()
