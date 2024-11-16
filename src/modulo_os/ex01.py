import os

#Executando comandos no terminal
os.system('cls')
os.system('echo "Hello World"')

#utlizando caminhos com os.path
caminho = os.path.join('Desktop','Curso','arquivo.txt')
print(os.path.split(caminho))
print(os.path.splitext(caminho))
print(os.path.exists('C:\\Users\\joser\\OneDrive\\Documentos\\MeusRepositórios\\Exercicios-python\\src\\modulo_os\\ex01.py'))
print(os.path.abspath('.'))
print(os.path.basename(caminho))

