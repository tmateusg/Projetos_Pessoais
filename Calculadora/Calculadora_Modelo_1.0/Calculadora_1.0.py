from time import sleep

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
    opção = int(input('Que deseja fazer? '))
    if opção == 1:
        soma = numero1 + numero2
        print(f'A soma entre {numero1} e {numero2} é = {soma}')
    elif opção == 2:
        subtração = numero1 - numero2
        print(f'A subtração entre {numero1} e {numero2} é = {subtração}')
    elif opção == 3:
        multiplicação = numero1 * numero2
        print(f'A multiplicação entre {numero1} e {numero2} é = {multiplicação}')
    elif opção == 4:
        divisão = numero1 / numero2
        print(f'A divisão entre {numero1} e {numero2} é = {divisão}')
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
