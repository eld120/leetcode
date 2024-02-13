'''
Write a function that takes a string word as an argument and returns a count of all of the “A”s in that string.
'''


def number_of_a_found(word: str) -> int:
    counter = 0
    for char in word:
        # unsure if I should cover both upper and lower case
        if char == 'a' or char == 'A':
            counter+= 1
    return counter



def test_one():
    assert number_of_a_found('aardvark') == 3

def test_two():
    assert number_of_a_found('seyamack') == 2

def test_three():
    assert number_of_a_found('SEYAMACK') == 2

def test_five():
    assert number_of_a_found('AardvArk') == 3