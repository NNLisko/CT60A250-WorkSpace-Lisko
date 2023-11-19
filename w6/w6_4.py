def create_matrix():
    rows = int(input("Enter the number of rows:\n"))
    columns = int(input("Enter the number of columns:\n"))
    matrix = []
    for i in range(rows):
        c = input(f"Give row {i + 1}:\n").split()
        while len(c) != columns:
            print("Error: Invalid number of elements in the row. Please try again.")
            c = input(f"Give row {i + 1}:\n").split()
        x = [eval(i) for i in c]
        matrix.append(list(x))
    return matrix


def print_matrix(matrix):
    for i in matrix:
        print("|", end="")
        print(*i, sep="\t", end="")
        print("|")


matrix = create_matrix()
print_matrix(matrix)
