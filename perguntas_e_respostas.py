perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
for questao in perguntas:
    print(questao['Pergunta'])
    for indices, opção in enumerate(questao['Opções']):
        print(f'{indices + 1}) {opção}')
    opção_usuario = input('Escolha uma opção: ')
    try:
        alternativa_usuario = questao['Opções'][int(opção_usuario) - 1]
    except ValueError:
        print('ERROU!!')
        continue
    except IndexError:
        print('ERROU!!')
        continue

    alternativa_correta = questao['Resposta']

    if alternativa_usuario == alternativa_correta:
        print('ACERTOU!!')
        acertos += 1
    else:
        print('ERROU!!')
qtd_de_perguntas = len(perguntas)
print(f'Você acertou {acertos} de {qtd_de_perguntas} perguntas')