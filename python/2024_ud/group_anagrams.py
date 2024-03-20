from typing import List


def group_anagrams(strs: List[str]) -> List[str]:
    ans = dict()
    keys = set()
    for chars in strs:
        hashable = "".join(sorted(chars))
        if hashable not in keys:
            keys.add(hashable)
            
            ans[hashable] = [chars]
        else:
            ans[hashable] += [chars]
    return ans.values()