def input_integers():
    c = input("Give integers separated by comma:\n")
    n2 = int(input("Give an integer:\n"))
    newlist = []
    final = []
    for i in c:
        if i in newlist:
            pass
        else:
            newlist.append(i)
    for j in range(n2 + 1):
        final.append(min(newlist))
        newlist.remove(min(newlist))
    print(f"{n2}th smallest element is {max(final)}")


input_integers()
