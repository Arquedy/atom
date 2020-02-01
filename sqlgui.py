from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):

        self.windows_ratio = Tk()
        self.frame1 = Frame(self.windows_ratio)
        self.radio_value = IntVar()
        self.radio_value.set(0)
        self.label1 = Label(self.windows_ratio, text =  'O que deseja fazer?')
        self.cadastrar = Radiobutton(self.windows_ratio, text = 'Cadastrar', variable = self.radio_value, value = 1)
        self.consultar_nome = Radiobutton(self.windows_ratio, text = 'Consulta', variable = self.radio_value, value = 2)
        self.alterar = Radiobutton(self.windows_ratio, text  = 'Alterar dados', variable = self.radio_value, value = 3)
        self.consulta_geral = Radiobutton(self.windows_ratio, text = 'Ver dados clientes', variable = self.radio_value, value = 4)

        self.label1.pack(anchor = 'w')
        self.cadastrar.pack(anchor = 'w')
        self.consultar_nome.pack(anchor = 'w')
        self.alterar.pack(anchor = 'w')
        self.consulta_geral.pack(anchor = 'w')

        self.frame2 = Frame(self.windows_ratio)
        self.botao = Button(self.frame2, text = 'Aceitar', command = self.exibir)
        self.quit = Button(self.frame2, text = 'Sair', command = self.quit1)

        self.botao.pack(side = 'left')
        self.quit.pack(side = 'left')

        self.frame1.pack()
        self.frame2.pack()

        mainloop()

    def exibir(self):
        pass

    def quit1(self):
        pass

minha = MinhaGUI()
