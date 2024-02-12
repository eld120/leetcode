"""
What is the longest word that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated. Make sure your solution can handle ties.
"""


def word_stuff():
    with open("../sowpods.txt", "r") as file:
        longest_words_with_rstlne = ""

        word_length = 0
        for line in file:
            word = line.rstrip("\n")
            for char in word:
                if char not in "RSTLNE":
                    break
            else:
                if len(word) > word_length:
                    word_length = len(word)
                    longest_words_with_rstlne = word
                elif len(word) == word_length:
                    longest_words_with_rstlne += f", {word}"
            continue
        print(longest_words_with_rstlne)


if __name__ == "__main__":
    import timeit

    timed = timeit.timeit(word_stuff, number=1)
    print(f"run took {timed *1000} ms")
