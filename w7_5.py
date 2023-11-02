def csvanalyze(fileName):
    with open(fileName, "r+") as f:
        for line in f:
            line = line.split(", ")
            print(line[1])


fileName = input("Give the name of the CSV file:\n")
csvanalyze(fileName)
