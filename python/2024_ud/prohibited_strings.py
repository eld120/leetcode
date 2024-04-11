

def prohibited_stings(prohibited: list[str], username: str) -> bool:
    '''
    Write a function that takes two arguments, a list of prohibited strings and a username, and returns a boolean of whether or not the username contains any of the prohibited strings.

    Some important details:

    - The list of prohibited words will provide words in some casing, and we want to be case-insensitive in our checks. For example, if “darn” is a prohibited word, “darn”, “DARN” and “DaRn” are all prohibited.
    - Sometimes people like to make usernames that substitute numbers for letters, to try to get around a prohibited word list. We also want to make those substitutions prohibited. The specific letter substitutions we need to check are:
        - A becomes 4
        - E becomes 3
        - I becomes 1
        - O becomes 0
        - For example, if “darn” is a prohibited word, “d4rn” is also a prohibited word. If “darn” and “heck” are prohibited words, the username “D4RN_y0u_T0_h3ck” contains prohibited words.
    '''
    # insert lowercase values of prohibited strings into set
    # prohibited_set = {set(x.lower()) for x in prohibited}
    prohibited_ = [name.split() for name in prohibited]
    # split username into a list of characters
    username_chars = [char.lower() for char in username]
    # dict of specific letter substitutions
    letter_substitutions = {4: 'a', 3: 'e', 1: 'i', 0: 'o'}
    # checking substring.lower() of username is in prohibited
    for name in prohibited:
        
        left = 0
        right = 1
        prohibited_sub = name.split()
        for i, char in enumerate(prohibited_sub):
            try:
                if int(char) in letter_substitutions:
                    prohibited_sub[i] = letter_substitutions[int(char)]
            except ValueError:
                prohibited_sub[i] = char.lower()
        while right < len(prohibited_sub):
            if prohibited_sub[left:right] in username.lower():
                pass
            # xDarn
        
        
        # if _ is the first of both username and prohibited - contin
    
        # continue to check the first char of all other prohibited strings
        # if we find a prohibited string return True
                


def proh_strs(prohibited: list[str], username: str) -> bool:
    conversions = {4: 'a', 3: 'e', 1: 'i', 0: 'o'}
    
    prohibited = [x.lower() for x in prohibited]
    
    username_list = [s.lower() for s in username]
    for i, char in enumerate(username_list):
        if char in '0123456789' and int(char) in conversions:
            username_list[i] = conversions[int(char)]
    user = "".join(username_list)
    for word in prohibited:
        if word in user:
            return True
    return False

def test_username_contains_bad_words():
    assert proh_strs(['damn', 'shit'], 'fuckshitdamn') == True

def test_username_valid():
    assert proh_strs(['damn', 'ass'], 'Danny') == False

def test_prohibited_at_beginning():
    assert proh_strs(['damn', 'fuck'], 'd4mnshitdam') == True
