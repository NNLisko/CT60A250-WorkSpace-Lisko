def occurrences(ch, string):
    value = 0
    for i in range(len(string)):
        if string[i] == ch:
            value += 1
    return value

char = input('Enter a character:\n')

if len(char) != 1:
    print('Error: Give a single character.')
    exit(0)

str = input('Enter a string:\n')

print(f"The character '{char}' appears {occurrences(char, str)} time(s) in the string.")


