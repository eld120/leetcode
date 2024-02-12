"""
What are all of the words that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.
"""


if __name__ == "__main__":
    with open("../sowpods.txt", "r") as file:
        words_containing_only_rstlne = ""
        for line in file:
            word = line.rstrip("\n")
            for letter in word:
                if letter not in "RSTLNE":
                    break
            else:
                words_containing_only_rstlne += word + ", "
            continue

    print(words_containing_only_rstlne)
