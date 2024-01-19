'''
1.1: Implement an algorithm to determine if a string has all unique characters. What if we can't use additional data structures
'''


def is_unique(word: str) -> bool:
    stuff_found = set()
    for w in word:
        if w not in stuff_found:
            stuff_found.add(w)
        else:
            print(False)
            return False
    print(True)
    return True


data_one = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
data_two = '123456789'
data_three = '11'

if __name__ == '__main__':
    is_unique(data_one)
    is_unique(data_two)
    is_unique(data_three)
