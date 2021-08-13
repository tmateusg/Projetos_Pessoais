def valida_numero(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('ERRO! Digite um número valido.')
        else:
            return float(entrada)


def operacoes(numero1, numero2):
    soma = numero1 + numero2
    #subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    print(f'A soma de {numero1} + {numero2} = {soma:.2f}')
    #print(f'A subtracao de {numero1} - {numero2} = {subtracao:.2f}')
    print(f'A multiplicacao de {numero1} * {numero2} = {multiplicacao:.2f}')
    print(f'A divisao de {numero1} / {numero2} = {divisao:.2f}')
    print('#' * 40)


def escolha():
    from time import sleep
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
