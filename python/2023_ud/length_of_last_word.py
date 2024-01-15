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
from string import ascii_letters

# leetcode is fucking up again

def length_of_last_word(s: str)-> int:
    counter = -1
    letter_counter = 0
    if len(s) == 1:
        print(1)
        return len(s)
    while counter + len(s) >= 0:
        if s[counter] in ascii_letters:
            
            letter_counter += 1
            counter -= 1
        elif s[counter] == ' ' and letter_counter == 0:
            
            counter -= 1
            continue
        else:
            print(letter_counter)
            return letter_counter
    print(letter_counter)
    return letter_counter
        
test_one = "luffy is still joyboy"
test_two =  "   fly me   to   the moon  "
test_three  = "Hellow World"
test_four = "a " 
test_five = " a"


if __name__ == '__main__':
    length_of_last_word(test_three)