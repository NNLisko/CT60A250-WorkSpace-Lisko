def reverse_string(C):
    if len(C) == 1:
        return C
    else:
        return reverse_string(C[1:]) + C[0]

C = input("Give a string to reverse:\n")
print(f"Original String: {C}")
print(f"Reversed String: {reverse_string(C)}")
