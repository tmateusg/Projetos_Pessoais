from PySimpleGUI import PySimpleGUI as psg
from Funções_Preço_Justo import *
import math

#Layout
psg.theme('Reddit')
layout = [
    [psg.Text('Cotação'), psg.Input(key='Cotação', size=(30, 1))],
    [psg.Text('LPA'), psg.Input(key='LPA', size=(30, 1))],
    [psg.Text('VPA'), psg.Input(key='VPA', size=(30, 1))],
    [psg.Button('Preço Justo')], #psg.Input(key='Preço Justo', size=(30, 1))],
    [psg.Output(size=(50, 5))]

]
#Janela
janela = psg.Window('Calculadora de Preço Justo', layout)


#ler os eventos
while True:
    evento, valores = janela.read()
    if evento == psg.WINDOW_CLOSED:
        break
    #if evento == 'Calcular':


