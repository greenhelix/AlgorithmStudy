def isWordPalindrome(word):
    return word == word[::-1]


sample1 = "aibohphobia"
sample2 = "hehehehehe"
print(isWordPalindrome(sample1))
print(isWordPalindrome(sample2))
