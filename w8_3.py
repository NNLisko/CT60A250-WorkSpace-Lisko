from datetime import datetime

def Time():
    inputtime = input("Give a datetime string in format \"%Y/%m/%d %H:%M:%S\":\n")
    date = datetime.strptime(inputtime, "%Y/%m/%d %H:%M:%S")
    print(f"Month: {date.strftime('%B')}\nWeekday: {date.strftime('%A')}\nWeek nr: {date.strftime('%W')}\nDay nr: {date.strftime('%j')}")

Time()