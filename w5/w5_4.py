def compressor(string):
    if len(string) == 0:
        return ''
    r = ''
    this = string[0]
    count = 1
    for ch in range(1, len(string)):
        if string[ch] == this:
            count += 1
        elif count == 1:
            r += this
            this = string[ch]
        else:
            r += this + str(count)
            this = string[ch]
            count = 1
    if count == 1:
        r += this
    else:
        r += this + str(count)
    return r
    
word = input('Give a string to compress:\n')

compressed = compressor(word)
print(f'Compressed string: {compressed}')
print(f"Compressing ratio {round(len(compressed)/len(word), 2)}")
