n1 = int(input('Enter the first number:\n'))
n2 = int(input('Enter the second number:\n'))

print('The calculator can perform the following operations:')
print('1) Add')
print('2) Subtract')
print('3) Multiply ')
print('4) Divide')
print(f'The numbers you entered are {n1} and {n2}')
choise = int(input('Select the operation (1-4):\n'))

if choise == 1:
    print(f'Selection 1: {n1} + {n2} = {round(n1 + n2, 2)}')
elif choise == 2:
    print(f'Selection 2: {n1} - {n2} = {round(n1- n2, 2)}')
elif choise == 3:
    print(f'Selection 3: {n1} * {n2} = {round(n1 * n2, 2)}')
elif choise == 4:
    if n2 == 0:
        print('Error: Zero cannot be used as a divisor.')
    else:
        print(f'Selection 4: {n1} / {n2} = {round(n1 / n2, 2)}')
else:
    print('This operator was not recognized.')