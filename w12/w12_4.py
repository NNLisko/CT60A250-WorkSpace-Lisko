def euclid(n1, n2):
    if n2==0:
        return n1
    else: return euclid(n2, n1%n2)

n = input("Give two positive integers separated by comma:\n").split(", ")
n1, n2 = int(n[0]), int(n[1])
print(f"gcd({n1},{n2}) = {euclid(n1, n2)}")
 Missing newline at the end of file.
