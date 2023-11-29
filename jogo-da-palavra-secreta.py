#desenvolver um jogo em que o usuário tem que adivinhar a palavra secreta a partir de suas letras
import os
palavra_secreta = 'ornitorrinco'
qtd_letras = len(palavra_secreta)
letras_acertadas = ''
qtd_tentativas = 0
palavra_formada = ''
while palavra_formada != palavra_secreta:
    palavra_formada = ''
    tentativa_letra = input('\nDigite uma letra: ')

    if len(tentativa_letra) != 1: #validação
        print('Digite somente uma letra!')
        continue

    qtd_tentativas += 1
    if tentativa_letra in palavra_secreta:
        letras_acertadas += tentativa_letra
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    os.system('cls')
    print(palavra_formada)

print(f'Você Ganhou!!!!\nA palavra secreta era {palavra_secreta}\nForam necessárias {qtd_tentativas} tentativas')

