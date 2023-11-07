from datetime import datetime as dt

def time():
    correct = None
    try:
        date1 = dt.strptime(input("Enter a date in YYYY-MM-DD format:\n"), "Y-m-d")
    except ValueError:
        correct = False
    else:
        correct = True
    print(correct)

time()