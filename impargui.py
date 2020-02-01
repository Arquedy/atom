from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        self.windows = Tk()
        self.frame1 = Frame(self.windows)
        self.label1 = Label(self.frame1, text = 'Vamos ver se esse numero é primo ou n')
        self.entrada = Entry(width = 30, bg = 'blue', fg = 'black')
        self.label1.pack(side = 'left')
        self.entrada.pack(side = 'left')

        self.frame2 = Frame(self.windows)
        self.botao = Button(self.frame2, text = 'Calcular', command = self.impar)
        self.botao.pack(anchor = 'center')

        self.frame1.pack()
        self.frame2.pack()

        mainloop()

    def impar(self):
        x = int(self.entrada.get())
        result = x % 2
        if result == 0:
            messagebox.showinfo('Resultado', 'Nao é impar')
        else:
            messagebox.showinfo('Resultado', 'Eh impar')

minha = MinhaGUI()
