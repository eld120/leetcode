'''
What are all of the words that have only “U”s for vowels?
'''

if __name__ == '__main__':
    with open('../sowpods.txt', 'r') as file:
        words_with_U_as_vowels = tuple()
        for line in file:
            word = line.rstrip('\n')    
            # need to revisit truth tables perhaps
            #if "U" in word and not any(letter not in word for letter in 'AEIOU'):  
            if "U" in word and not 'A' in word and not 'E' in word and not 'I' in word and not 'O' in word:
                words_with_U_as_vowels += (word,)

    print(words_with_U_as_vowels)