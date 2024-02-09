'''
Create and print an array containing all of the words that have a U but no other vowel.
'''

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        result = []

        not_this = {'A', 'E', 'I', 'O'}
        for line in f.readlines():
            word = line.rstrip('\n')
            if 'A' not in word and 'E' not in word and 'I' not in word and 'O' not in word and 'U' in word:
                result.append(word)

            
        print(result)