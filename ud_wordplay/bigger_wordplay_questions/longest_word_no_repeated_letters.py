from typing import List


"""
words is an array of strings
"""
# def find_longest_word_no_repeated_letters(words):    
def sowpods_parser():
    with open('../sowpods.txt', 'r') as file:
        return [line.rstrip('\n') for line in file]



def find_longest_word_no_repeated_letters(words: List[str]):
    """
    What is the longest word where no letter is used more than once?

    Is there more than one? And what does the function want?

    - What are all the longest words ...
    - What is the first word in the list that is the longest without ... 
    """
    
    longest_words = []
    longest_word_length = 0

    for word in words:
        
        letter_tracker = set()
        if len(word) < longest_word_length:
            continue
        for letter in word:
            if letter not in letter_tracker:
                letter_tracker.add(letter)

        if len(word) != len (letter_tracker):
            continue

        if len(word) > longest_word_length:
            longest_words = [word]
            longest_word_length = len(word)
        elif len(word) == longest_word_length:
            longest_words.append(word)
        
    return longest_words
    



def test_one():
    
    assert ["DERMATOGLYPHICS", "UNCOPYRIGHTABLE"] == find_longest_word_no_repeated_letters(sowpods_parser())


if __name__ == "__main__":
    print(find_longest_word_no_repeated_letters(sowpods_parser()))
