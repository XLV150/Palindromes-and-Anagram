def is_palindrome(string):
    return string[::-1] == string

word = input("Enter a word to check if its an Palindrome: ")

if is_palindrome(word):
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))

def is_anagram():
    string1 = input("Enter the first word: ")
    string2 = input("Enter the second word: ")
    if sorted(string1) == sorted(string2):
        print("{} and {} are anagrams.".format(string1, string2))
    else:
        print("{} and {} are not anagrams.".format(string1, string2))


is_anagram()

def is_anagra1(x, y):
    if sorted(x) == sorted(y):
        print("{} and {} are anagrams.".format(x, y))
    else:
        print("{} and {} are not anagrams.".format(x, y))


