'''

    - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
    - For example, “FEEDBACK” is an answer to this question



'''
from typing import List, Tuple

# function that parses sowpods.txt
# return a list 
def parse_file(file_path: str) -> List: 
    with open(file_path, 'r') as file: # pylint: disable=W1514
        return [line.rstrip('\n') for line in file]


def alphabet_chain(sowpods_list=parse_file('C:/Users/seyam/Sandbox/l33tcode/leetcode/ud_wordplay/sowpods.txt')):
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
    


def find_longest_alphabet_chain_in_file(file_path: str)-> Tuple[List[str], List[str]]:
    '''
    given all of the words in sowpods find the longest alphabet chain, words that are m
    '''
    # parse sowpods
    sowpods = parse_file(file_path)
    # vars: longest_chain , list_of_words (words made from longest alphabet chains)
    alphabet_chains = dict()
    longest_chain_length = 0
    # for every word in sowpods call (longest_alphabet chain)
    for word in sowpods:
        #current_alphabet_chain = longest_alphabet chain method
        current_alphabet_chain = longest_alphabet_chain_in_word(word)
        hashable_chain = "".join(sorted(current_alphabet_chain))
        # if len(current_alphabet chain) > len(longest_chain) then current becomes the longest
        if len(current_alphabet_chain) > longest_chain_length:
            longest_chain_length = len(current_alphabet_chain)
            alphabet_chains = dict()
            alphabet_chains[hashable_chain] = [word]


        elif len(current_alphabet_chain) == longest_chain_length:    
            if hashable_chain not in alphabet_chains.keys():
                alphabet_chains[hashable_chain] = [word]
            else:
                alphabet_chains[hashable_chain] += [word]



    print(longest_chain_length)
    return alphabet_chains

    






def test_feedback():
    assert alphabet_chain(['FEEDBACK', 'NOTAWORD', '', 'FEEDBACKS', 'ZZZ']) == ['FEEDBACK', 'FEEDBACKS']

def test_longest_chain_turquoised():
    assert longest_alphabet_chain_in_word('TURQUOISED') == ['Q', 'R', 'S', 'T', 'U']




if __name__ == '__main__':
    print(find_longest_alphabet_chain_in_file('C:/Users/seyam/Sandbox/l33tcode/leetcode/ud_wordplay/sowpods.txt'))