w1 = input('Enter word 1:\n')
w2 = input('Enter word 2:\n')

if w1 < w2:
    print(f"'{w1}' comes earlier in order than '{w2}'.")
elif w2 < w1:
    print(f"'{w2}' comes earlier in order than '{w1}'.")
else:
    print('The words are the same.')

if 'z' in w1 and 'z' in w2:
    print(f"Letter 'z' is found in the word '{w1}'")
    print(f"Letter 'z' is found in word '{w2}'")
elif 'z' not in w1 and 'z' not in w2:
    print("The letter 'z' was not found in either of the words.")
else:
    if 'z' in w1:
        print(f"Letter 'z' is found in word '{w1}'.")
    if 'z' in w2:
        print(f"Letter 'z' is found in word '{w2}'.")

w3 = input('Enter a word to be tested:\n')

if w3 == w3[::-1]:
    print(f"'{w3}' is a palindrome.")
else:
    print(f"'{w3}' is not a palindrome.")