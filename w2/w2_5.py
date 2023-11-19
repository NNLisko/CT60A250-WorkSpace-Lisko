print('This program calculates the average of the 3 numbers you enter.')
print('The numbers can be int\'s or float\'s')
n1 = float(input('Enter the first number:\n'))
n2 = float(input('Enter the second number:\n'))
n3 = float(input('Enter the third number:\n'))

summ = n1 + n2 + n3

print(f'Sum of the numbers: {round(summ,3)}')

print(f'Average of the numbers (rounded to 3 decimal places): {round(summ / 3, 3)}')
print(f'Average of the numbers (rounded to the closest integer): {round(summ / 3)}')
print(f'Average of the numbers as an integer without the decimal part: {round(summ // 3)}')
