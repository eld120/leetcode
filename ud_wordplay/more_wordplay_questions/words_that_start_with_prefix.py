'''


[ ] Write a function that takes a string `prefix` as an argument and returns an array of all of the words that start with that prefix (the prefix has to be at the beginning of the word).
'''

def find_prefixes(string_prefix):
    with open('../sowpods.txt', 'r') as file:
        prefix_matches = []
        for line in file:
            word = line.rstrip('\n')
            prefix_length = len(string_prefix)
            if string_prefix == word[:prefix_length]:
                prefix_matches.append(word)

    print(prefix_matches)
            
    


if __name__ == '__main__':
    find_prefixes('PY')