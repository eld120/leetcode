from typing import List
'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

def longestCommonPrefix(strs: List[str]) -> str:
    if strs[0] == "":
        return ""
    counter = 1
    while counter <= len(strs[0]):
        # take slice of first value
        try:
            #breakpoint()
            slices = strs[0][:counter]
            # compare slice of first value to all other values
            for val in strs:
                #breakpoint()
                if val[:counter] == slices:
                    #print(f'{val[:counter]} == {slices}')
                    continue
            # if slice exists in all values continue, else return slice -1
                else:
                    print(strs[0][:counter - 1])
                    return strs[0][:counter - 1]
            # if counter is less than 1, there are no matches, else slice -1 should return the slice
            
        except IndexError:
            # return no matches or the previous slice
            #print('anything')
            print(strs[0][:counter - 1])
            return strs[0][:counter - 1]
        #print(counter)
        counter += 1
    #print('why is this skipped')
    print(strs[0][:counter])
    return strs[0][:counter]


test_one = ["flower","flow","flight"]
test_two = ["flower","flower","flower","flower"]
test_three = ["dog","racecar","car"]
four  = [""]
five = ["ab", "a"]
if __name__ == '__main__':
    longestCommonPrefix(five)