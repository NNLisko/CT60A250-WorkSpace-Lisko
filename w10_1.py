def input_integer(count): 
    j=1
    l = []
    while j <= count:
        try:
            n1 = int(input("Enter an integer:\n"))
            j += 1
            l.append(n1)
        except:
            print("Invalid input.  Please enter an integer.")
    print(f"The sum of the entered integers is: {sum(l)}")

while True:
    try:
        count = int(input("Enter an integer:\n"))
        break
    except:
        print("Invalid input. Please enter an integer.")
        

print(f"Now give {count} integers!")
input_integer(count)