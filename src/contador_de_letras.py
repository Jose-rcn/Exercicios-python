#Desenvolver um programa empython capaz de contar o caractere que mais se repete dentro de uma string
phrase = input('Write a phrase:')
most_repeated_char = ''
count_most_repeated_char = 0
index = 0
while index < len(phrase):
    if phrase[index] == ' ': #eliminar espaços
        index+=1
        continue
    actual_char = phrase[index]
    count_actual_char = phrase.count(actual_char)
    if count_actual_char > count_most_repeated_char:
        most_repeated_char = phrase[index]
        count_most_repeated_char = count_actual_char
    index += 1
print(f'The most repeated letter in this sentence is "{most_repeated_char}" which ocurred {count_most_repeated_char} times')
