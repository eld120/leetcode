'''Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''

def palindrom(x: int) -> bool:
    stringy = str(x)
    counter = 0
    left = 0
    right = -1
    while counter < len(stringy)//2:
        l_left = stringy[left]
        l_right = stringy[right]
        if l_left == l_right:
            left += 1
            right -= 1
            counter += 1
            continue
        else:
            return False
    return True 


test_one = 10
test_two = -121
test_three = 121
test_four = 12345
test_five = 1001
if __name__ == '__main__':
    palindrom(test_five)