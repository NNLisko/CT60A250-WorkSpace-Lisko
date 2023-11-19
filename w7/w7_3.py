import shutil as sh


def file_copy(fileA, fileB):
    fileA = open(fileA, "r+")
    fileB = open(fileB, "a+")
    sh.copyfileobj(fileA, fileB)
    print("File copied successfully!")


file1 = input("Please give the name of the source file:\n")
file2 = input("Please give the name of the destination file:\n")
file_copy(file1, file2)
