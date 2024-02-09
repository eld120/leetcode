'''

[ ] What countries use only one vowel in their name (the vowel can be used multiple times)
    - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.
'''
from collections import Counter


if __name__ == '__main__':
    with open('./countries.txt', 'r') as file:
        # O(n^2) time complexity
        countries_with_one_vowel = []
        for line in file:
            country = line.rstrip('\n')
            vowels_found = {letter.lower() for letter in country if letter in 'aeiou'}
            if len(vowels_found) < 2:
                countries_with_one_vowel.append(country)

        print(countries_with_one_vowel)