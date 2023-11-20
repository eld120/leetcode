'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
from string import ascii_letters

def valid_palindrome(string: str)-> bool:
    ascii_stuff = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if [s.lower() for s in string if s in ascii_stuff] == [ t.lower() for t in list(reversed(string)) if t in ascii_stuff]:
        return True
    else:
        return False
    
test_one = "A man, a plan, a canal: Panama"


if __name__ == '__main__':
    valid_palindrome(test_one)