"""
What are all of the words that have only “E”s for vowels and are at least 15 letters long?
"""

if __name__ == "__main__":
    with open("../sowpods.txt") as file:
        letters_with_E_as_vowels = ""
        for line in file:
            word = line.rstrip("\n")
            if (
                len(word) > 14
                and "E" in word
                and "A" not in word
                and "I" not in word
                and "O" not in word
                and "U" not in word
            ):
                letters_with_E_as_vowels += word + ", "

    print(letters_with_E_as_vowels)
