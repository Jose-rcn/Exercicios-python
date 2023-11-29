import os
lista_de_compras = []
opcao = ''
while True:
    print('Selecione uma opção')
    opcao = input('[I]nserir    [A]pagar    [L]istar    [E]ncerrar: ').lower()
    if opcao == 'i':
        produto_inserir = input('Informe o produto a ser inserido: ')
        lista_de_compras.append(produto_inserir)
    elif opcao == 'a':
        if not lista_de_compras:
            print('Lista vazia! Insira itens primeiro')
            continue
        for indice, produto in enumerate(lista_de_compras):
            print(indice + 1, '-', produto)
        produto_apagar = input('Informe o indice do produto a ser apagado: ')
        try:
            lista_de_compras.pop(int(produto_apagar)-1)
        except:
            print('Indice Inválido')
            continue
    elif opcao == 'l':
        if not lista_de_compras:
            print('Lista vazia! Insira itens primeiro')
        for indice, produto in enumerate(lista_de_compras):
            print(indice + 1, '-', produto)
        continue
    elif opcao == 'e':
        print('Encerrando programa! ')
        break
    else:
        print('Opção Inválida! Tente novamente')
        continue
    os.system('cls')
