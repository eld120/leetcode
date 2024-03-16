

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_dict = dict()
    values = set()
    keys = set()
    for index, char in enumerate(s):
        if t[index] in values and char not in keys:
            return False
        elif char not in keys:
            s_dict[char] = t[index]
            keys.add(char)
            values.add(t[index])
        elif s_dict[char] != t[index] :
            return False
    return True
    



def test_badc():
    assert is_isomorphic('badc', 'baba') == False