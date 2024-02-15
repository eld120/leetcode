from typing import List


def find_longest_word_no_repeated_letters():
    """
    What is the longest word where no letter is used more than once?
    """
    with open("../sowpods.txt", "r") as file:
        longest_word = ""
        longest_word_length = 0

        for line in file:
            word = line.rstrip("\n")
            letter_tracker = set()
            for letter in word:
                if letter in letter_tracker:
                    break
                else:
                    letter_tracker.add(letter)

            else:
                if len(word) > longest_word_length:
                    longest_word = word
                    longest_word_length = len(word)
                elif len(word) == longest_word_length:
                    longest_word += f",{word}"

    print(f"{longest_word} is/are the longest word(s) at {longest_word_length} letters")


def test_one():
    """
    what i thought was a bug was really my code finding another word of the
    same length but both words were concatenated so I thought it was the an error in my logix
    """
    longest_word = ""
    longest_word_length = 0
    file = ["DERMATOGLYPHICS", "DERMATOGLYPHICSUNCOPYRIGHTABLE"]
    for line in file:
        word = line.rstrip("\n")
        letter_tracker = set()

        for letter in word:
            # breakpoint()
            if letter in letter_tracker:
                # breakpoint()
                break
            else:
                # breakpoint()
                letter_tracker.add(letter)
        else:
            # breakpoint()
            if len(word) > longest_word_length:
                # breakpoint()
                longest_word = word
                longest_word_length = len(word)
            elif len(word) == longest_word_length:
                # breakpoint()
                longest_word += word
    assert longest_word == "DERMATOGLYPHICS"


if __name__ == "__main__":
    find_longest_word_no_repeated_letters()
