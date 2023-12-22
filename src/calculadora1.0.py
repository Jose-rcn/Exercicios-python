# Desenvolver uma calculadora com as funções de soma, multiplicação, divisão e subtração usando a estrutura de repetição while
import os
from time import sleep
while True:
    print('[1] Somar', '[2] Subtrair', '[3] Multiplicar', '[4] Dividir', '[5] Sair do programa', sep='\n')
    opcao = input('Escolha uma opção: ')
    opcao_int = 0
    try:
        opcao_int = int(opcao)
        if opcao_int == 5:
            break
    except:
        print('Você não digitou um número.')
        sleep(3)
        os.system('cls')
        continue
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    if opcao_int == 1:
        print('A soma dos número informados é', num1 + num2)
    elif opcao_int == 2:
        print('A subtração dos número informados é', num1 - num2)
    elif opcao_int == 3:
        print('A multiplicação dos número informados é', num1 * num2)
    elif opcao_int == 4:
        try:
            print('A divisão dos número informados é', num1 / num2)
        except ZeroDivisionError:
            print('A divisão por zero resulta em uma indeterminação!')
    else:
        print('\nOpção Inválida!\nTente novamente')
    sleep(3)
    os.system('cls')

    

