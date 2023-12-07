def integer_sum(n):
    if n <= 1:
        return n
    else:
        return n + integer_sum(n-2)

n1 = int(input("Give a non-negative integer n:\n"))
print(f"n + (n-2) + (n-4) + ... = {integer_sum(n1)}")
