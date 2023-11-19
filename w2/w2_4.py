#takes a word as an input
word = input('Give a word:\n')

#prints
print(f'The length of the word is {len(word)}')

#takes int as an input
n1 = int(input(f'Give an integer smaller than or equal to {len(word)}:\n'))

#prints the word and replaces nth character with *
print(word[:n1 - 1] + '*' + word[n1:])
