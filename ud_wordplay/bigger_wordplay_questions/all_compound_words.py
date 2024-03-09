def parse_sowpods_set():
    with open("../sowpods.txt", "r") as file:
        return {line.rstrip("\n") for line in file}


# iterate through the list
# we're looking for words that contain more than one other word

# compound_words = []
# for line in file:
#     for word in file:
#         if word in line and word != line:
#             compound_words.append(line)
# rolling hash set?
"""
['SNOW', 'SNOWMAN', 'BEACHBALL', 'BEACH', 'BALL', 'FLKSLDKF']
['SNOWMAN', 'BEACHBALL']

What are all of the compound words? These are words made up of 2 smaller words. For example, “SNOWMAN” is a compound word made from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from “BEACH” and “BALL”

- create a container for compound words
- iterate through sowpods
- iterate through every word in sowpods
- take slice of the first word in sowpods 
- the remainder of the first word and check if both exist in the set
- If both exist


"""


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
        letter_index = 0
        is_compound_word = False
        while letter_index < len(word) - 1 and not is_compound_word:
            if word[: letter_index + 1] and word[letter_index + 1 :] in file:
                compound_words.add(word)
                is_compound_word = True
            letter_index += 1

    return compound_words


def test_one():
    assert "BEACHBALL" in find_compound_words_optimized(
        ["SNOW", "MAN", "SNOWMAN", "BEACHBALL", "BEACH", "BALL", "FLKSLDKF"]
    )
    assert "SNOWMAN" in find_compound_words_optimized(
        ["SNOW", "MAN", "SNOWMAN", "BEACHBALL", "BEACH", "BALL", "FLKSLDKF"]
    )

def test_omission():
    assert "SNOWMAN" not in find_compound_words_optimized(
        ["SNOW", "SNOWMAN", "BEACHBALL", "BEACH", "BALL", "FLKSLDKF"]
    )


def test_validate():
    assert (
        "SNOWMAN"
        and "SUPEREXCELLENT"
        and "BACKSIGHTS" in find_compound_words_optimized()
    )
