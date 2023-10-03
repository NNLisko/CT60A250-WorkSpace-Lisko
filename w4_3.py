s1 = input('Enter a string:\n')
value = 0
for ch in s1:
    if ch == 'a' or ch == 'A':
        value += 1
    elif ch == 'e' or ch == 'E':
        value += 1
    elif ch == 'i' or ch == 'I':
        value += 1
    elif ch == 'o' or ch == 'O':
        value += 1
    elif ch == 'u' or ch == 'U':
        value += 1
print(f'Number of vowels is: {value}')