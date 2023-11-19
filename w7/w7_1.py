def write_names(File):
    now = open(File, "w")
    n = input("Enter a name or 'stop':\n")
    while n != "stop":
        now.write(f"{n}\n")
        n = input("Enter a name or 'stop':\n")
    now.close()


fileName = input("Enter the name of the file to be saved:\n")
write_names(fileName)
