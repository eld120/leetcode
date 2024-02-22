'''

    - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
    - For example, “FEEDBACK” is an answer to this question



'''
from typing import List

# function that parses sowpods.txt
# return a list 
def parse_sowpods() -> List:
    with open('../sowpods.txt', 'r') as file:
        return [line.rstrip('\n') for line in file]


def alphabet_chain(sowpods_list=parse_sowpods()):
    # create a list of words that contain an alphabet chain
    alphabet_chain_words = []
    # iterate through the list of sowpod words
    for line in sowpods_list:
        # create is alphabet chain boolean flag
        contains_alphabet_chain = True
        # turn word into set
        word = set(line)
        # iterate through the list of alphabet chain letters
        for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
    
            
            if letter not in word:
                contains_alphabet_chain = False
            
        
        # if boolean flag is true then append to the list of alphabet chain words
        if contains_alphabet_chain:
            alphabet_chain_words.append(line)
    # return list of alphabet chain words
    return alphabet_chain_words


def test_feedback():
    assert alphabet_chain(['FEEDBACK', 'NOTAWORD', '', 'FEEDBACKS', 'ZZZ']) == ['FEEDBACK', 'FEEDBACKS']



if __name__ == '__main__':
    print(alphabet_chain())