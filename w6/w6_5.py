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


def print_matrix(matrix, matrix_transpose):
    print("The original matrix:")
    for i in matrix:
        print("|", end="")
        print(*i, sep="\t", end="")
        print("|")
    print("Its transpose:")
    for j in matrix_transpose:
        print("|", end="")
        print(*j, sep="\t", end="")
        print("|")


def transpose(matrix):
    columns = len(matrix[0])
    rows = len(matrix)
    res = [[0 for c in range(rows)] for x in range(columns)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[j][i] = matrix[i][j]
    return res


matrix = create_matrix()
matrix_transpose = transpose(matrix)
print_matrix(matrix, matrix_transpose)
