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

    print(f'A soma de {numero1} + {numero2} =           {soma:.2f}')
    print(f'A subtração de {numero1} - {numero2} =      {subtracao:.2f}')
    print(f'A multiplicacao de {numero1} * {numero2} =  {multiplicacao:.2f}')
    print(f'A divisao de {numero1} / {numero2} =        {divisao:.2f}')
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
            print('Finalizado...')
            break
        else:
            print('Opção invalida, tente novamente!')
        sleep(2)
    print('Fim da consulta!')
