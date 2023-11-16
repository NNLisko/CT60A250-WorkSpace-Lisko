import os

def isfile(f):
    try:
        with open(f, "r") as f:
            print(f"File content:\n{f.read()}")
    except:
        print("Error: File not found.")

f = input("Enter the file name:\n")
isfile(f)
