def parse_sowpods_set():
    with open("../sowpods.txt", "r") as file:
        return {line.rstrip("\n") for line in file}


def find_compound_words(file=parse_sowpods_set()):
    # initial 5 min O(n^2) implementation
    compound_words = []

    for line in file:
        for word in file:
            if word != line and line in word:
                compound_words.append(word)
    return compound_words


def find_compound_words_optimized(file=parse_sowpods_set()):
    # better I think but still O(m*n) time complexity
    compound_words: set = set()

    for word in file:
        substring = []
        letter_index = 0
        while letter_index < len(word) - 1:
            substring.append(word[letter_index])
            if "".join(substring) in file:
                compound_words.add(word)
            letter_index += 1

    return compound_words


def test_validate():
    assert (
        "SNOWMAN"
        and "SUPEREXCELLENT"
        and "BACKSIGHTS" in find_compound_words_optimized()
    )
