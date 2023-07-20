def reverseVowels(s: str) -> str:
    # string -> (vowel, index) -> string
    vowels = set("aeiouAEIOU")

    vowel_set = [letter for letter in s if letter in vowels]

    answer = ""
    decrement = -1
    for letter in s:
        if letter in vowels:
            answer += vowel_set[decrement]
            decrement -= 1
        else:
            answer += letter
    return answer
    # print(answer)


if __name__ == "__main__":
    reverseVowels("sweatshop")
