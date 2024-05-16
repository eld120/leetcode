from collections import Counter, defaultdict



scores = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}
 # if every char's count in scrabble_rack >= char count for the dict_sowpods
def is_valid_scrabble_word(scrabble_rack_dict, sowpod_letter_dict):
    '''
    ex 1: 
        rack = 'ABCD'
        word = 'CAB'

    ex 2:
        scrabble_rack_dict = 'ABCD'
        sowpod_letter_dict = 'CAT'

    ex 3: 
     scrabble_rack = 'ABB_'
    sowpod = 'ABBA'
    '''
    # count of wildcards
    wildcards = 0
    for char, count in scrabble_rack_dict.items():
        if char == '_':
            wildcards += 1

    for char, count in sowpod_letter_dict.items():
        # is char == _ then continue
        if scrabble_rack_dict[char] < count: 
            # if scrabble_rack_dict[char] + wildcards < count
            if scrabble_rack_dict[char] + wildcards >= count:
                # wildcard = scrabble_rack_dict[char] + wildcars - count
                wildcards = scrabble_rack_dict[char] + wildcards - count
            else:
                # else return false            
                return False
    return True
    



def scrabble_solver(scrabble_rack: str, path_to_word_list: str) -> str:
    '''
    Write code that:

    - Accepts a string (e.g. as an argument to a function, or as a command-line argument). This string represents your Scrabble “rack”.
    - Prints out the words that can be made from the characters in that input string, along with their Scrabble scores, one word per line, in descending score order

    Example input and output:

    `$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
    `17 piques`
    `17 equips`
    `16 quips`
    `16 pique`
    `16 equip`
    `15 quip`
    '''
    # init counter of chars in letters
    scrabble_rack_count = Counter(scrabble_rack.lower())
    # init defaultdict of scores and words
    valid_scrabble_words = defaultdict(list)
    # open sowpods in read mode as file
    with open(path_to_word_list, 'r') as file:

        # for every line in sowpods
        for line in file:

            # remove the newline character
            word = line.rstrip('\n')
            # counter of characters for the line in sowpods
            sowpod_letter_count = Counter(word.lower())
           
            if is_valid_scrabble_word(scrabble_rack_count, sowpod_letter_count):
                # we'll calculate the score, init score
                # for char, count in dict_sowpods 
                score = 0
                for char, count in sowpod_letter_count.items():
                    # score += scores[char] * count
                    score += scores[char] * count
                    
                # answers[score] += [line]
                valid_scrabble_words[score] += [word.lower()]
    # for score in sorted(answers)
    test_list = []
    for score in sorted(valid_scrabble_words):
        # for word in answers[score]
        for word in valid_scrabble_words[score]:
            # print(f'{score} {word})
            print(f'{score} {word}')
            test_list.append((score, word))
    return test_list





def test_scrabble_base_case():
    assert scrabble_solver('SPCQEIUABCD','./scrabble_words.txt' ) == [(7, 'cab')]



def test_valid_scrabble_word():
    assert is_valid_scrabble_word(Counter('SPCQEIUABCD'.lower()), Counter('cab')) == True


def test_handle_wildcards():
    assert is_valid_scrabble_word(Counter('abb_'), Counter('abba')) == True

def test_failing_wildcards():
    assert is_valid_scrabble_word(Counter('abb_'), Counter('aaba')) == False

def test_failing_two_wildcards():
    assert is_valid_scrabble_word(Counter('abb__'), Counter('aabat')) == False