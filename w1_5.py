n1 = input('Give the first integer: ')
n2 = input('Give the first integer: ')

div = round(int(n1) // int(n2),1)
rmd = round(int(n1) % int(n2),1)

print(f'The number {n2} Goes to number {n1} {div} times')
print(f'The reminder is {rmd}')
