#takes two integers as input
n1 = input('Give the first integer: ')
n2 = input('Give the first integer: ')

#divides input integers
div = round(int(n1) // int(n2),1)

#calculates and rounds the remainder
rmd = round(int(n1) % int(n2),1)

#prints
print(f'The number {n2} Goes to number {n1} {div} times')
print(f'The reminder is {rmd}')
