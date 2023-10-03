yesno = input('Do you want to stop the execution of the program (y/Y):\n')

if yesno == 'Y' or yesno == 'y':
    print('Bye!')

elif yesno == 'n' or yesno == 'N':
    usr = input('Enter username:\n')
    pswrd = input('Enter password:\n')
    if usr == 'Mark' and pswrd == 'drowssap':
        print('User recognized.')
    else:
        print('You entered an invalid login name or password.')
