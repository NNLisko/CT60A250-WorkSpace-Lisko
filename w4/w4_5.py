s1 = input('Enter a string:\n')
str = ''

for ch in s1:
    if ch == 's':
        str += 'z'
    elif ch == 'S':
        str += 'Z'
    else:
        str += ch
print(f'Modified string: {str}')
