import string
import random

letters = string.ascii_letters
digits = string.digits
special = string.punctuation
comb = letters + digits + special

def randomPassword():
    random.seed(8292)
    length = int(input("Enter the length of the password:\n"))
    while length <= 0:
        print("Password length must be a positive integer.")
        length = int(input("Enter the length of the password:\n"))
    password = random.sample(comb, length)
    print(f"Generated password {''.join(password)}")

randomPassword()