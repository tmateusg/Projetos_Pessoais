from tkinter import *
import math

def calcular():
    vpa = float(box_vpa.get())
    lpa = float(box_lpa.get())
    preco_justo = math.sqrt((22.5 * vpa * lpa))
    Resp.set(str(round(preco_justo, 2)))


#JANELA
janela = Tk()
#janela.title('Calculadora Preço Justo')
janela.geometry('200x200+500+300')
janela.resizable(False, False)
Resp = StringVar() #

#MOLDURA
moldura_janela = Frame(janela)

#Etiquetas
lbl_Tit = Label(janela,
                text='Digite os Valores',
                font='Arial 12',
                justify=CENTER,
                fg='black')

lbl_vpa = Label(moldura_janela,
                text='Valor de VPA',
                font='Arial 10',
                fg='red',
                justify=CENTER)

lbl_lpa = Label(moldura_janela,
                text='Valor de LPA',
                font='Arial 10',
                fg='red',
                justify=CENTER)

lbl_Espaco = Label(moldura_janela,)

lbl_preco = Label(moldura_janela,
                  text='Preço Justo',
                  font='Arial 10',
                  justify=CENTER)

lbl_Resp = Label(moldura_janela,
                 textvariable=Resp,
                 font='Arial 10',
                 width=6,
                 bd=2, relief='solid',) #

#Caixas de Texto
box_vpa = Entry(moldura_janela,
                font='Arial 11',
                justify=CENTER,
                bg='orange',
                width=6)
box_vpa.focus()

box_lpa = Entry(moldura_janela,
                font='Arial 11',
                justify=CENTER,
                bg='orange',
                width=6)

#Botao
btn_preco = Button(moldura_janela, text='Calcular', command=calcular)


#posicionamento
lbl_Tit.grid(row=0, column=0,)
lbl_vpa.grid(row=0, column=0,)
lbl_lpa.grid(row=1, column=0, sticky='w')
lbl_Espaco.grid(row=2, column=0)
lbl_preco.grid(row=3, column=0)
lbl_Resp.grid(row=3, column=1)
box_vpa.grid(row=0, column=1)
box_lpa.grid(row=1, column=1)
btn_preco.grid(row=4, column=1)

moldura_janela.grid()
janela.mainloop()
