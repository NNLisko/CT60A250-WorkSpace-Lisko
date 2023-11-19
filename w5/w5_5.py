def is_word_in(w1, w2):
  c = len(w1)
  v = len(w2)
  for i in range(v):  #v - c + 1
    for j in range(c):
      if w2[i + j] != w1[j]:
        break
    if j + 1 == c:
      return i
  return -1

w1 = input("Enter the first string:\n")
w2 = input("Enter the second string:\n")

substring = is_word_in(w1, w2)

if substring == -1:
  print(f"The first string cannot be found in the second string.")
else:
  print(f"The first string can be found in the second string.")
