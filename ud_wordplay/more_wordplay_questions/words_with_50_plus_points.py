"""

[ ] Let’s assign letters the following points:
    - W = 12
    - Z = 15
    - E = -17
    - All other letters = 1

What are all of the words with at least 50 points?
"""

if __name__ == "__main__":
    with open("../sowpods.txt", "r") as file:
        points_exceptions = {"W": 12, "Z": 15, "E": -17}
        words_with_at_least_fifty = ""

        for line in file:
            word = line.rstrip("\n")
            points_counter = 0
            for char in word:
                if char in points_exceptions:
                    points_counter += points_exceptions[char]
                else:
                    points_counter += 1

            if points_counter > 49:
                words_with_at_least_fifty += f"{word}, "

        print(words_with_at_least_fifty)
