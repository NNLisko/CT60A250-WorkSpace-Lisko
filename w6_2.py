def input_integers():
    c = input("Give integers separated by comma:\n").split(",")
    global n
    n = int(input("Give an integer:\n"))
    if n > len(c):
        return -1
    sortlist = []
    for i in range(len(c)):
        c[i] = eval(c[i])
    for i in c:
        if i not in sortlist:
            sortlist.append(i)
    final = []
    for j in range(n):
        final.append(min(sortlist))
        sortlist.remove(min(sortlist))
    return max(final)


value = input_integers()

if value == -1:
    print("Not suitable")
else:
    print(f"{n}th smallest element is {value}")
