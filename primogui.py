from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        self.windows = Tk()
        self.windows.title('Primos')
        self.frame1 = Frame(self.windows)
        self.label1 = Label(self.frame1, text = 'Vamos ver se o numero é primo ou nao')
        self.entrada = Entry(width = 30)
        self.label1.pack(side = 'left')
        self.entrada.pack(side = 'left')

        self.frame2 = Frame(self.windows)
        self.label2 = Label(self.frame2,text = 'O numero digitado ')
        self.label_dinamica = StringVar()
        self.label3 = Label(self.frame2, textvariable = self.label_dinamica)
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')


        self.frame3 = Frame(self.windows)
        self.botao = Button(self.frame3, text = 'Mostrar', command = self.primos)
        self.botao_sair = Button(self.frame3, text = 'Encerrar', command = self.quit)
        self.botao.pack(side = 'left')
        self.botao_sair.pack(side = 'left')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        mainloop()

    def primos(self):
        try:
            num = int(self.entrada.get())
        except:
            y = messagebox.askquestion('Erro', 'Vc ja viu uma letra sendo numero primo?')
            if y == 'yes':
                messagebox.showinfo('AFF', 'Te fude vai')
                self.quit()

        n = num
        #joguei um divisor com base 2
        div = 2
        # e condicionei que primo eh verdadeiro
        e_primo = True

        while div < n and e_primo:
            if n % div == 0:
                e_primo = False
            div = div + 1

        if e_primo and n != 1:
            x ='Eh primo'
            self.label_dinamica.set(x)
        else:
            x = 'N eh primo'
            self.label_dinamica.set(x)
    def quit(self):
        quit()

minha = MinhaGUI()
