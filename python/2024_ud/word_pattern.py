

def word_pattern(pattern: str, s: str)-> bool:
    '''
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
    Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
    '''
    if len(pattern) != len(s):
        return False

    mapping = dict()
    values =  set()
    keys = set()
    flag = True
    second = s.split(' ')
    if len(pattern) != len(second):
        return False
    for index, char in enumerate(pattern):
        
        if char in keys and second[index] not in values:
            flag = False
        elif char not in keys and second[index] in values:
            flag = False
        
        else:
            try:
                if mapping[char] != second[index]:
                    flag = False
            except KeyError:
                mapping[char] = second[index]
                values.add(second[index])
                keys.add(char)
    return flag


def test_one():
    assert word_pattern('abba', 'dog cat cat fish') == False

def test_two():
    assert word_pattern('abba', 'dog cat cat dog') == True

def test_three():
    assert word_pattern('abba', 'dog dog dog dog') == False

def test_four():
    assert word_pattern('aba', 'dog cat cat') == False