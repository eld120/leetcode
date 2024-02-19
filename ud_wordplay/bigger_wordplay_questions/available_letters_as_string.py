from typing import List

def handle_sowpods():
    with open('./sowpods.txt', 'r') as file:
        # had to change from a generator expression to a list comp because the file is closed 
        return [line.rstrip('\n') for line in file]
    


# let's come back to arrays
def find_available_letters(letter_string: str, word_list=handle_sowpods()):
    '''
    Write a function that takes a string availableLetters as an argument and returns an array of all of the words that can be made from only those letters. Letters can be re-used as many times as needed and can appear in any order. Not all of the letters in availableLetters have to be used.
    '''
    
    available_letters = set(letter_string)
    
    words_with_available_letters = []

    for word in word_list:
        for letter in word:
            if letter not in available_letters:
                break
        else:
            words_with_available_letters.append(word)
    return words_with_available_letters



def test_one():
    assert find_available_letters('') == []

def test_two():
    assert 'CAMEL' in find_available_letters('ACELM') 
