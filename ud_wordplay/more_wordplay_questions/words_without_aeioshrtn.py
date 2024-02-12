"""
What is the longest word that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)? Make sure your solution can handle ties.
"""


if __name__ == "__main__":
    with open("../sowpods.txt", "r") as file:
        longest_word_i_could_conjur = ""
        longest_word_length = 0
        for line in file:
            word = line.rstrip("\n")
            for char in word:
                if char in "AEIOSHRTN":
                    break
            else:
                if len(word) > longest_word_length:
                    longest_word_length = len(word)
                    longest_word_i_could_conjur = word
                elif len(word) == longest_word_length:
                    longest_word_i_could_conjur += f", {word}"
            continue
    print(longest_word_i_could_conjur)
