def analyze(analyzefile):
    File = open(analyzefile, "r+")
    wordcount = 0
    rowcount = 0

    for line in File:
        rowcount += 1
        filewords = line.split()
        wordcount += len(filewords)

    print(f"Number of lines: {rowcount}\nNumber of words: {wordcount}")


analyzefile = input("Give the text file to analyze:\n")
analyze(analyzefile)
