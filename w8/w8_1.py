import math

def sin():
    deg = float(input("Enter an angle in degrees:\n"))
    rad = deg * (math.pi/180)
    sin = math.sin(rad)
    print(f"The sine of {deg} degrees is {round(sin, 3)}\n")
    menu()

def cos():
    deg = float(input("Enter an angle in degrees:\n"))
    rad = deg * (math.pi/180)
    cos = math.cos(rad)
    print(f"The cosine of {deg} degrees is {round(cos, 3)}\n")
    menu()

def arcSin():
    sine = float(input("Enter the sine value:\n"))
    if sine > 1 or sine < -1:
        print("Invalid input. Sine value must be between -1 and 1.\n")
        menu()
    rad = math.asin(sine)
    deg = rad * (180/math.pi)
    print(f"The inverse sine (in degrees) of {sine} is {round(deg, 3)}\n")
    menu()

def arcCos():
    cosine = float(input("Enter the cosine value:\n"))
    if cosine > 1 or cosine < -1:
        print("Invalid input. Cosine value must be between -1 and 1.\n")
        menu()
    rad = math.acos(cosine)
    deg = rad * (180/math.pi)
    print(f"The inverse cosine (in degrees) of {cosine} is {round(deg, 3)}\n")
    menu()

def menu():
    print("Trigonometric Calculations:\n1. Sine Calculation\n2. Cosine Calculation\n3. Inverse Sine Calculation\n4. Inverse Cosine Calculation\n5. Exit")
    choice = int(input("Enter your choice (1/2/3/4/5):\n"))
    while choice < 0 or choice > 5:
        print("Invalid choice. Please select a valid option.\n")
        print("Trigonometric Calculations:\n1. Sine Calculation\n2. Cosine Calculation\n3. Inverse Sine Calculation\n4. Inverse Cosine Calculation\n5. Exit")
        choice = int(input("Enter your choice (1/2/3/4/5):\n"))
    if choice == 1:
        sin()
    elif choice== 2:
        cos()
    elif choice== 3:
        arcSin()
    elif choice== 4:
        arcCos()
    elif choice== 5:
        print("Bye!")
        exit(0)

menu()
