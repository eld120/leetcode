'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

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
from collections import deque

def isPalindrome( sinput: str) -> bool:
    # stringify = [letter for letter in s if letter in ascii_letters]
    # if len(sinput) == 1:
    #     return True
    letter_set = set(ascii_letters + '0123456789')
    
    right = -1
    left  = 0
    count_of_letters = 0
    left_adjust = 0
    right_adjust = 0
    is_palindrome = True
    while is_palindrome:
        if left >= len(sinput) - 1 or right *-1 > len(sinput):
            return is_palindrome
             
        if sinput[left] not in letter_set and sinput[right] not in letter_set:
            left += 1
            left_adjust += 1
            right -= 1
            right_adjust += 1
        elif sinput[left] not in letter_set:
            left += 1
            left_adjust += 1
        elif sinput[right] not in letter_set:
            right -= 1
            right_adjust += 1       
        elif sinput[right] in letter_set and sinput[left] in letter_set and sinput[right].lower() != sinput[left].lower():
            is_palindrome = False
            count_of_letters += 1
        elif right *-1 > len(sinput)//2 + 1 + right_adjust or left  > len(sinput)//2 + left_adjust:
            break
        
        else:
            right -= 1
            left += 1
            count_of_letters += 1

        
    if count_of_letters > 0:
        return is_palindrome
    else: 
        return not is_palindrome
    # need to exclude strings with numbers and ignore punctuation with valid characters but exclude punctuation without characters




def test_one():
    assert isPalindrome(" ") == True

def test_two():
    assert isPalindrome("race a car") == False

def test_three():
    assert isPalindrome("amanaplanacanalpanama ") == True

def test_four():
    assert isPalindrome("0P") == False


def test_wtf():
    assert isPalindrome("a.b,.") == False

def test_i_am_tired():
    assert isPalindrome(".,") == True

def test_wtf_edgecases():
    assert isPalindrome("a.") == True

def test_failing_everything_now():
    assert isPalindrome("1b1") == True

def test_fucking_edgecases():
    assert isPalindrome("......a.....") == True