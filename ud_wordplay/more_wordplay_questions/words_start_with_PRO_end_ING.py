"""
What are all of the words that start with “PRO”, end in “ING”, and are exactly 11 letters long?
"""

if __name__ == "__main__":
    with open("../sowpods.txt") as file:
        pro_ing_words = ""
        for line in file:
            word = line.rstrip("\n")
            if len(word) == 11 and word[:3] == "PRO" and word[-3:] == "ING":
                pro_ing_words += word + ", "

    print(pro_ing_words)
