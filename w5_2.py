def count_words(sen):
    v = 1
    for ch in sen[::]:
        if ch == ' ':
            v += 1
    return v

sen = input('Give a sentence:\n')

print(f"This sentence contains {count_words(sen)} words.")