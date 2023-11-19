#takes a year as an int input
y1 = int(input('Enter a year:\n'))

#if-elif-else to determine if the year is a leap year
if y1 % 100 == 0 and not y1 % 400 == 0:
    print(f'{y1} is not a leap year.')
elif y1 % 4 == 0:
    print(f'{y1} is a leap year.')
else:
    print(f'{y1} is not a leap year.')
