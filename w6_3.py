def input_integers():
    waa = input("Give integers separated by comma:\n")
    aaw = waa[::-1].split(",")
    newlist = []
    for i in aaw:
        newlist.append(int(i))
    print(f"Reversed list: {newlist}")


input_integers()
