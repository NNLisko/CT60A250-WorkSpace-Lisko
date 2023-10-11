def input_integers():
    global c
    c = input("Give integers separated by comma:\n").split(",")
    listint = []
    newlist = []
    for i in c:
        newlist.append(int(i))
    for i in c:
        if int(i) not in listint:
            listint.append(int(i))
        elif int(i) in listint:
            pass
    print(f"Original List: {newlist}")
    return listint


print(f"List with duplicates removed: {input_integers()}")
