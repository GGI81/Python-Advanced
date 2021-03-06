# 9.	Recursion Palindrome

def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))  # abcba is a palindrome
print(palindrome("peter", 0))  # peter is not a palindrome
