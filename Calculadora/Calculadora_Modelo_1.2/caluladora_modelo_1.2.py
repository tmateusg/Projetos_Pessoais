from time import sleep
from funcoes_DEF import *


numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 6:
    print('''
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [5] Digitar novos numeros
    [6] Sair da consulta''')
    opção = int(input('O que deseja fazer? '))
    if opção == 1:
        soma(numero1, numero2)
    elif opção == 2:
        subtracao(numero1, numero2)
    elif opção == 3:
        multiplicacao(numero1, numero2)
    elif opção == 4:
        divisao(numero1, numero2)
    elif opção == 5:
        print('Digite novos valores:')
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    elif opção == 6:
        print('Finalizado...')
    else:
        print('Opção invalida, tente novamente!')
    sleep(1)
print('Fim da consulta!')