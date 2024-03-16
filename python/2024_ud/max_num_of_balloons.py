from collections import Counter



def max_num_baloons(text: str) -> int:
    '''
    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of instances that can be formed.
    '''
    lowest_num = 99999
    
    count = Counter(text)
    for char in 'balloon':
        try:
            count[char]
        except KeyError:
            return 0
        
        if char == 'l' or char == 'o':
            lowest_num = min(lowest_num, count[char]//2)
        else:
            lowest_num = min(lowest_num, count[char])
    
    return lowest_num


def test_one():
    assert max_num_baloons('nlaebolko') == 1

def test_two():
    assert max_num_baloons('loonbalxballpoon') == 2

def test_zero():
    assert max_num_baloons('leetcode') == 0