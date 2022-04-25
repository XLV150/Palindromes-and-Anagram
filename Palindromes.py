def is_palindrome(string):
    return string[::-1] == string

word = input("Enter a word to check if its an Palindrome: ")

if is_palindrome(word):
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))
