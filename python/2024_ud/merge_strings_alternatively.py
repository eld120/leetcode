

def merge_alternatively(word1: str, word2: str) -> str:
    shorter = len(word1) if len(word1) < len(word2) else len(word2)
    
    new_str = []
    index = 0
    while index < shorter:
        new_str.append(word1[index])
        new_str.append(word2[index])
        index += 1
    return "".join(new_str)+ word1[shorter:] + word2[shorter:]


def test_one():
    assert merge_alternatively("abc","pqr" )== "apbqcr"

def test_two():
    assert merge_alternatively("ab", "pqrs" ) == "apbqrs"

def test_three():
    assert merge_alternatively("abcd", "pq") == "apbqcd"