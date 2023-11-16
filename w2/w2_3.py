#takes word as an input
word = input('Enter a long word:\n')

#prints different indexings of the word
print(f'The first five letters are: {word[:5]}')
print(f'The last five letters are: {word[-5:]}')
print(f'Letters 2, 3, 4 and 5 are: {word[1:5]}')
print(f'Every second letter of the word: {word[1::2]}')
print(f"The word backwards '{word[::-1]}'")
