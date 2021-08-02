from time import sleep

def soma(numero1, numero2):
    soma= numero1 + numero2
    print(f'A soma de {numero1} + {numero2} é = {soma}')
    print('#' * 30)


def subtracao(numero1, numero2):
    subtracao = numero1 - numero2
    print(f'A subtracao de {numero1} - {numero2} é = {subtracao}')
    print('#' * 30)


def multiplicacao(numero1, numero2):
    multiplicacao= numero1 * numero2
    print(f'A multiplicacao de {numero1} * {numero2} é = {multiplicacao}')
    print('#' * 30)


def divisao(numero1, numero2):
    divisao = numero1 / numero2
    print(f'A divisao de {numero1} / {numero2} é = {divisao}')
    print('#' * 30)


def novos(numero1, numero2):
    print('Digite novos valores:')
    numero1 = int(input('Digite o primeiro valor: '))
    numero2 = int(input('Digite o segundo valor: '))

#proprama principal
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
        novos(numero1, numero2)
    elif opção == 6:
        print('Finalizado...')
    else:
        print('Opção invalida, tente novamente!')
    sleep(1)
print('Fim da consulta!')
