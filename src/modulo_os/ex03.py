import os
from itertools import count

caminho_dir = 'C:\\Users\\joser\\OneDrive\\Documentos\\MeusRepositórios\\Exercicios-python\\src'
counter = count()

for root,dirs,files in os.walk(caminho_dir):
    print(next(counter))
    print(root)
    print(dirs)
    print(files)