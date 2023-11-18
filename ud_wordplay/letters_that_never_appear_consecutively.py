'''
What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?
'''
from string import ascii_uppercase

tracker  = {letter*2 : False for letter in ascii_uppercase}

arr = []

if __name__ == '__main__':
    with open('./sowpods.txt', 'r') as f:
        for line in f.readlines():
            for letters in tracker:
                if letters in line:
                    tracker[letters] = True
        for value in tracker:
            if tracker[value] == False:
                arr.append(value)

        print(arr)
                    
