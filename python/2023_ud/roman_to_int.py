'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

def roman_to_int( s: str) -> int:
    VARS = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    ans  = 0
    counter = 0
    enumerated = tuple(s)
    for value in enumerated:
        if counter > 0:
            if VARS[enumerated[counter -1]] >= VARS[value]:
                ans += VARS[value]
            elif VARS[enumerated[counter -1]] < VARS[value]:
                ans += (VARS[value] -VARS[enumerated[counter -1]]*2)
        else:
            ans += VARS[value]
        counter += 1
    print(ans)
test_one = "MCMXCIV" # 1000 + 100 + (1000-200)+10+(100-20)+1+(5-2)
test_two = "XIV"
test_three = "XVI"
if __name__ == '__main__':
    roman_to_int('MCMXCIV')