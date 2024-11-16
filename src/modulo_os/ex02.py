import os

#listando diretorio
caminho_dir = 'C:\\Users\\joser\\OneDrive\\Documentos\\MeusRepositórios\\Exercicios-python\\src'
arquivos = os.listdir(caminho_dir)
for arquivo in arquivos:
    caminho_completo = os.path.join(caminho_dir,arquivo)
    if not os.path.isdir(caminho_completo):
        print(arquivo)
        continue
    print(f'\033[1;32m{arquivo}')
    for item in os.listdir(caminho_completo):
        print('\t',item)
    print('\033[m',end='')