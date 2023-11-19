#takes amount of points (int) as an input
points = float(input('Enter your number of points:\n'))

#assigns grade based on points
if points <= 100 and points >= 90:
    print('Your grade is: 5')
elif points < 90 and points >= 80:
    print('Your grade is: 4')
elif points < 80 and points >= 70:
    print('Your grade is: 3')
elif points < 70 and points >= 60:
    print('Your grade is: 2')
elif points < 60 and points >= 50:
    print('Your grade is: 1')
elif points > 100:
    print('How')
else:
    print('Your grade is: 0')
