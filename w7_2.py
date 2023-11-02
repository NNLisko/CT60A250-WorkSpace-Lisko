def print_names(fileName):
    c = open(fileName, "r+")
    c = list(c.read().split("\n"))
    print(*sorted(c), sep="\n")


fileName = input("Give the name of the input file:\n")
print_names(fileName)
