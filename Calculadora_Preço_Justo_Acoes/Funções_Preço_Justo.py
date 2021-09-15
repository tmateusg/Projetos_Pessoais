import math

def cabeçario():
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
    Cotação = valida_numero('Digite o valor da cotação: R$ ')
    Lpa = valida_numero('Digite o lucro por ação (LPA): R$ ')
    Vpa = valida_numero('Digite Valor por ação (VPA): R$ ')
    Preço_Justo = math.sqrt((22.5 * Lpa * Vpa))
    print(f'\033[0;34mO preço justo da ação é:\033[m \033[1;31mR$ {Preço_Justo:.2f}\033[m')
    Margem_Segurança = ((Preço_Justo / Cotação)-1) * 100
    if Preço_Justo > Cotação:
        print(f'\033[1;32mComprar!\033[m O valor da ação esta abaixo \033[1;32m{Margem_Segurança:.2f}%\033[m do preço justo.')
    else:
        print(f'\033[1;31mNÃO Comprar!\033[m O valor da ação esta acima \033[1;31m{(Margem_Segurança * -1):.2f}%\033[m do preço justo.')

    print('\033[4;33m\nOBS:Valor obtido tendo como referência a fórmula de Benjamim Graham.')
