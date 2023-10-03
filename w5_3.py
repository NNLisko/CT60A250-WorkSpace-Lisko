def anagram(A, B):
    return sorted(A) == sorted(B)

str1 = input('Enter string A:\n')
str2 = input('Enter string B:\n')

print(f"{str1} and {str2} are {'not ' if not anagram(str1, str2) else ''}anagrams")
