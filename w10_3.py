def div(n1, n2):
    try:
        div = n1/n2
        print(f"The result of {n1} / {n2} is {round(div, 8)}")
    except:
        print("You cannot divide by zero")

try:
    n1 = float(input("Enter the first number:\n"))
    n2 = float(input("Enter the second number:\n"))
    div(n1, n2)
except:
    print("You must enter valid numbers")
