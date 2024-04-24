'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

def group_anagrams(strs: list[str]) -> list[list[str]]:
    
    lookup = dict()
    for  val in strs:
        key = "".join(sorted(val))
        if key not in lookup:
            lookup[key] = [val]
        else:
            lookup[key].append(val)
    return lookup.values()

         