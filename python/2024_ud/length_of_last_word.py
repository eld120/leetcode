'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

def lengthOfLastWord(s: str) -> int:
    
    ret = []
    letter_count = 0
    for char in reversed(s):
        if char == ' ' and letter_count > 0:
            return len(ret)
        elif char != ' ':
            letter_count += 1
            ret.append(char)
    return len(ret)



def test_one():
    assert lengthOfLastWord("Hello World") == 5


def test_two():
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4

def test_three():
    assert lengthOfLastWord("luffy is still joyboy") == 6