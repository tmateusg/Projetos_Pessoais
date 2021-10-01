
import math


def cabecario():
    msg = 'Calculadora de Preço Justo de Ações'
    tam = len(msg) + 6
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)


def valida_numero(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('ERRO! Digite um número.')
        else:
            return float(entrada)


def consulta():
    Cotacao = valida_numero('Digite o valor da cotação: R$ ')
    Lpa = valida_numero('Digite o lucro por ação (LPA): R$ ')
    Vpa = valida_numero('Digite Valor por ação (VPA): R$ ')

    Preco_Justo = math.sqrt((22.5 * Lpa * Vpa))
    print(f'\033[0;34mO preço justo da ação é:\033[m \033[1;31mR$ {Preco_Justo:.2f}\033[m')
    Margem_Seguranca = ((Cotacao / Preco_Justo)-1) * 100
    if Preco_Justo > Cotacao:
        print(f'\033[1;32mComprar!\033[m O valor da ação esta abaixo \033[1;32m{Margem_Seguranca:.2f}%\033[m do preço justo.')
    else:
        print(f'\033[1;31mNÃO Comprar!\033[m O valor da ação esta acima \033[1;31m{(Margem_Seguranca * 1):.2f}%\033[m do preço justo.')

    print('\033[4;33m\nOBS:Valor obtido tendo como referência a fórmula de Benjamim Graham.')


