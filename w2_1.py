#takes name, integer and float as input
name = input('Enter your name:\n')
n1 = int(input('Enter an integer:\n'))
n2 = float(input('Enter a float:\n'))

#exponents the float with the integer
exp = round(n2 ** n1,2)

#prints
print(f'Decimal {n2} to power {n1} is {exp}\nThank you for using the program {name}!')
