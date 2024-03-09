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


def longest_alphabet_chain_in_word(input_string: str):
    '''
    given a string of uknown length eg 'FEEDBACK'
    
    -> FOODBUCK


    sorted word - 'ABCDEEFK' - needs to be compared to the alphabet 'ABCDEFG'
    also consider removing duplicates (perhaps turn the sorted word into a set)
    
    - need to define the start/end of the alphabet chain:
    base case is first letter in sorted word == beginning of the alphabet
        - find out where I need to start in the alphabet via a dictionary (key=letter, value=index in the alphabet)
        - if the first sorted letter in my word is C : we'd immediately know where to start looking in the alphabet
        - iterate through the letters in the sorted word, use dict lookup (or compare incrementing slice of word with slice of alphabet)


    
    TURQUOISED
    ['D', 'E', 'I', 'O', 'Q', 'R', 'S', 'T', 'U', 'U']
    need a variable to track the longest alphabet chain
    DE currently longest alphabet chain
    QRS currently longest alphabet chain
    QRST
    QRSTU is the longest alphabet 

    tracking the longest alphabet chain
    alphabet_chain_start and alphabet_chain_end pointers
    current_alphabet_chain
    

    FEEDBACK
    sorted(set(FEEDBACK))
    ['A', 'B', 'C', 'D', 'E', 'F', 'K']
    A
    AB
    ABC
    ABCD
    ABCDEF
    '''
    
    longest_alphabet_chain = []
    current_alphabet_chain = []
    #breakpoint()
    # ['D', 'E', 'I', 'O', 'Q', 'R', 'S', 'T', 'U', 'U']
    for char in sorted(set(input_string)):
        print(f'current_alphabet_chain: {current_alphabet_chain}')
        print(f'longest_alphabet_chain: {longest_alphabet_chain}')
        print(f'char: {char}')
        if not current_alphabet_chain:
            current_alphabet_chain.append(char)
        elif ord(current_alphabet_chain[-1]) + 1 == ord(char):
            current_alphabet_chain.append(char)
        else:
            if len(current_alphabet_chain) > len(longest_alphabet_chain):
                longest_alphabet_chain = current_alphabet_chain
            current_alphabet_chain = [char]
    if len(current_alphabet_chain) > len(longest_alphabet_chain):
        longest_alphabet_chain = current_alphabet_chain
    return longest_alphabet_chain
    





def test_feedback():
    assert alphabet_chain(['FEEDBACK', 'NOTAWORD', '', 'FEEDBACKS', 'ZZZ']) == ['FEEDBACK', 'FEEDBACKS']



if __name__ == '__main__':
    print(longest_alphabet_chain_in_word('TURQUOISED'))