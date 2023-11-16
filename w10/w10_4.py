def mtrx():
    mtrx = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    try:
        row = int(input("Enter the row index:\n"))
        col = int(input("Enter the column index:\n"))
        try:
            print(f"Value at position ({row}, {col}): {mtrx[row][col]}")
        except:
            print("Error: Index out of bounds. Please enter valid row and column indices.")
    except:
        print("Error: Please enter valid integers for row and column indices.")
mtrx()
