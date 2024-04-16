from string import ascii_letters
from collections import Counter


def most_common(paragraph: str, banned: list[str]) -> str:
    alphabet = set(ascii_letters)
    count = Counter()
    temp = []
    para = []
    for char in paragraph:
        if temp and char == " " or char == ",":
            para.append("".join(temp))
            temp = []
        elif char in alphabet:
            temp.append(char.lower())
    if temp:
        para.append("".join(temp))

    temp = []
    for  word in para:
        if word not in banned:
            count[word] += 1
   #breakpoint()
    return count.most_common(1)[0][0]
    

def test_one():
    assert most_common("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']) == 'ball'

def test_two():
    assert most_common('a.', [])

def test_bob():
    assert most_common('Bob', []) == 'bob'

def test_stupid():
    assert most_common('Bob. hIt, ball', ["bob", "hit"]) == 'ball'

def test_stupid_shit():
    assert most_common("a, a, a, a, b,b,b,c, c", ['a']) == 'b'