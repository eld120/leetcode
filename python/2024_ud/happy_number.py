'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 
Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
'''


    
    


def isHappy(n: int) -> bool:
    '''
    know the length of n
    # live coding implementation
    '''
    if n == 1:
        return True
    
    lol = set()
    
    answer = 0
    while True:

        for num in str(n):
            answer =+ int(num)**2
        if n in lol:
            return False
        else:
            lol.add(n)
        n = answer

        if n == 1:
            return True
    












def happy_number(number: int) -> bool:
    # revisted this the next day
    if number == 1:
        return True
    lol = set()
    
    answer = 0
    cyclic = False

    while not cyclic:
        answer = 0
        
        if number not in lol:
            lol.add(number)
        else:
            cyclic = True
            
        for num in str(number):
            
            answer += int(num)**2

        if answer == 1:
            return True
        
        number = answer
        

    return False

# note: this is a cycle detection problem, often solved using two pointers as a fast/slow pointer will eventually meet if a cycle exists
# alternatively a set tracking the values or ids of an object would do the same thing



def test_one():
    assert isHappy(19) == True

def test_two():
    assert isHappy(2) == False

# def test_three():
#     assert isHappy(3) == False

def test_refactor_one():
    assert happy_number(19) == True

def test_refactor_two():
    assert happy_number(2) == False

def test_refactor_three():
    assert happy_number(3) == False