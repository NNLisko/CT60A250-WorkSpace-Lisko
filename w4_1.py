n1 = int(input('Enter a non-negative integer:\n'))
f1 = n1

if n1 > 0:
    for i in range(1, n1):
        n1 *= i
    print(f'Factorial of {f1} is {n1}')

elif n1 == 0:
    print('Factorial of 0 is 1')

else:
    print('Error: Factorial is not defined for negative numbers')
