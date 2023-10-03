n1 = int(input('Enter a positive integer:\n'))

if n1 > 0:
    for i in range(2, n1 + 1, 2):
        print(i, end='...')
else:
    print(f'{n1} is not positive')