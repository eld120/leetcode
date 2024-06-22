


def first_palindrome(words: list[str]) -> str:
    for word in words:
        left = 0
        right = len(word) -1
        palindrome = True
        while left < right:

            if word[left] != word[right]:
                palindrome = False
                break
            left += 1
            right -= 1
        if palindrome:
            return word
    return ""


def i_guess_this_is_faster(words: list[str]) -> str:
    for word in words:
        if word[::-1] == word:
            return word
    return ""