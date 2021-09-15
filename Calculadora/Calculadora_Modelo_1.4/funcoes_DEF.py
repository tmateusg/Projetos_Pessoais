from time import sleep


def valida_numero(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('ERRO! Digite um número valido!')
        else:
            return float(entrada)


def operacoes(numero1, numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    print(f'A soma = {soma:15.2f}')
    print(f'A subtração = {subtracao:10.2f}')
    print(f'A multiplicacao = {multiplicacao:6.2f}')
    print(f'A divisao = {divisao:12.2f}')
    print('¬' * 40)


def escolha():
    opção = 0
    while True:
        print('''
    [1] Digitar novos numeros
    [2] Sair da consulta''')
        opção = int(input(''' O que deseja fazer? '''))
        if opção == 1:
            print('Digite novos valores:')
            numero1 = valida_numero('Digite o primeiro valor: ')
            numero2 = valida_numero('Digite o segundo valor: ')
            operacoes(numero1, numero2)
        elif opção == 2:
            print('Finalizando...')
            break
        else:
            print('Opção invalida, tente novamente!')
        sleep(2)
    print('Fim da consulta!')
