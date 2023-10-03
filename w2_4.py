word = input('Give a word:\n')
print(f'The length of the word is {len(word)}')

n1 = int(input(f'Give an integer smaller than or equal to {len(word)}:\n'))
print(word[:n1 - 1] + '*' + word[n1:])