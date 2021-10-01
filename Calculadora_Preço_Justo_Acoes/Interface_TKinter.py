from tkinter import *
from Funções_Preço_Justo import *


janela = Tk()
janela.title('Calcula Preço Justo de Ações')
janela.geometry('400x400')

orientacao = Label(janela, text='Preencha os valores abaixo')
orientacao.grid(column=0, row=0)

Lpa = Label(janela, text='Digite o LPA')
Lpa.grid(column=0, row=1, padx=150, pady=10)

Lpa = Label(janela, text='Digite o VPA')
Lpa.grid(column=0, row=2, padx=150, pady=10)

Botao = Button(janela, text='Calcular', command=consulta)
Botao.grid(column=0, row=3, padx=150, pady=10)

preco_justo = Label(janela, text='')
Botao.grid(column=0, row=4, padx=150, pady=10)




janela.mainloop()
