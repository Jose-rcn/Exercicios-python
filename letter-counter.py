phrase = input('Write a phrase:')
most_repeated = phrase[0]
counter = 0
while counter < len(phrase):
    count_actual_char = (phrase.count(phrase[counter]))
    if count_actual_char > most_repeated.count(most_repeated):
        most_repeated = phrase[counter]
    counter += 1
print(f'The most repeated letter in this sentence is "{most_repeated}"')