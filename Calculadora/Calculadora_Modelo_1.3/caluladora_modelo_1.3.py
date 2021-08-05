from funcoes_DEF import *
from time import sleep

numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))
opção = 0
while opção != 3:
    print('''
    [1] Realizar operações
    [2] Digitar novos numeros
    [3] Sair da consulta''')
    opção = int(input(''' O que deseja fazer? '''))
    if opção == 1:
        operacoes(numero1, numero2)
    elif opção == 2:
        print('Digite novos valores:')
        numero1 = float(input('Digite o primeiro valor: '))
        numero2 = float(input('Digite o segundo valor: '))
    elif opção == 3:
        print('Finalizado...')
    else:
        print('Opção invalida, tente novamente!')
    sleep(1)
print('Fim da consulta!')
