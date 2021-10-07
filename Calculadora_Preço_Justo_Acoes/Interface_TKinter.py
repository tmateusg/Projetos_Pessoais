from tkinter import *
import math

def calcular():
    vpa = float(box_vpa.get())
    lpa = float(box_lpa.get())
    preco_justo = math.sqrt((22.5 * vpa * lpa))
    Resp.set(str(round(preco_justo, 2)))



#JANELA
janela = Tk()
janela.title('Calculadora Preço justo de Ações')
#janela.geometry('300x100')
Resp = StringVar() #

#MOLDURA
moldura_janela = Frame(janela)

#ITENS
lbl_Tit = Label(janela, text='Digite os valores')
lbl_vpa = Label(moldura_janela, text='Valor de VPA')
lbl_lpa = Label(moldura_janela, text='Valor de LPA')
lbl_preco = Label(moldura_janela, text='Preço Justo')
lbl_Resp = Label(moldura_janela, textvariable=Resp) #
box_vpa = Entry(moldura_janela, justify=CENTER)
box_lpa = Entry(moldura_janela, justify=CENTER)
btn_preco = Button(moldura_janela, text='Calcular', command=calcular)

#box_vpa.insert(END, 0)
#box_lpa.insert(END, 0)
box_vpa.focus()

#Posicionamento
lbl_Tit.grid(row=0, column=0)
lbl_vpa.grid(row=0, column=0)
lbl_lpa.grid(row=1, column=0)
lbl_preco.grid(row=2, column=0)
lbl_Resp.grid(row=2, column=1)
box_vpa.grid(row=0, column=1)
box_lpa.grid(row=1, column=1)
btn_preco.grid(row=3, column=1)

moldura_janela.grid()

janela.mainloop()