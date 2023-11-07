from datetime import datetime as dt

def time():
    date1 = input("Enter the first date (DD.MM.YYYY):\n")
    date2 = input("Enter the second date (DD.MM.YYYY):\n")
    dateobj1 = dt.strptime(date1, "%d.%m.%Y")
    dateobj2 = dt.strptime(date2, "%d.%m.%Y")
    dif = dateobj1 - dateobj2
    print(f"The number of days between {date1} and {date2} is {abs(dif.days)} days.")

time()